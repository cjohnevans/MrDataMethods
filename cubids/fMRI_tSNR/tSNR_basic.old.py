import pika, sys, json, subprocess, numpy, os, math
import nibabel as nib
from pprint import pprint
from datetime import datetime


# deal with the .nii.gz file extension
def gz_fileparts( file ):
    [pp, nn] = os.path.split( file )
    ind = nn.find('.')
    pp = pp + '/'
    ext = nn[ind:len(nn)]
    nn = nn[0:ind]
    return [pp, nn, ext]


# function to return response
def rabbit_return(job, response):
    cred = pika.credentials.PlainCredentials(job["rmquser"], job["rmqpass"])
    conn = pika.BlockingConnection(pika.ConnectionParameters(job["rmqip"], 5672, '/', cred))
    rm = conn.channel()
    rm.queue_declare(queue="finished")
    rm.basic_publish(exchange="", routing_key="finished", body=json.dumps(response))
    conn.close()


def main(job):

    start = str(datetime.now(tz=None))

    outputs = []
    log = []
    brief = []

    step = str(job["step"])
    print(job["outdir"])
    outdir = job["outdir"] + "step_" + step + "/"
    subprocess.run(['mkdir', '-p', outdir])
    subprocess.run(['rm', '-rf', outdir + '*'])
    print(outdir)
    for i in job["inputs"]:
        image_file = i[0]["image_file"]
        [pp, nn, ext] = gz_fileparts(image_file)

        out_base = outdir + nn + '_tsnr_proc'
        out_text = outdir + nn + '_tsnr.txt'
        out_rms = out_base + '_mc_rel_mean.rms'

        mask_file = out_base + '_brain_mask.nii.gz'
        brain_file = out_base + '_brain.nii.gz'

        subprocess.run(['/cubric/software/cubids/core/fsl/fMRI_tSNR/tSNR_calc.sh', image_file, out_base, out_text])
        n = numpy.loadtxt(out_text)
        n = n.tolist()
        if n is list:
            n = n[0]
            if n is list:
                n = float(n[0])
        if math.isnan(n):
            n = -10

        v = numpy.loadtxt(out_rms)
        v = v.tolist()
        if v is list:
            v = v[0]
            if v is list:
                v = float(v[0])
        if math.isnan(v):
            v = -10

        img = nib.load(mask_file)
        pixdim = img.header["pixdim"]
        pixvol  = pixdim[1] * pixdim[2] * pixdim[3]
        imgdata = img.get_fdata()
        imgshape = img.shape
        print(imgshape)

        count = 0
        for x in range(imgshape[0]):
            for y in range(imgshape[1]):
                for z in range(imgshape[2]):
                    if imgdata[x, y, z] > 0:
                        count = count + 1

        vol = count * pixvol

        log.append({
            "parameter": "tsnr_by_movement",
            "y": n,
            "x": v,
            "key": nn,
        })

        log.append({
            "parameter": "tsnr_by_brainvol",
            "y": n,
            "x": vol,
            "key": nn,
        })

        brief.append({
            "type": "text",
            "viewer": "textViewer",
            "message": "Mean tSNR = " + str(n)
        })
        brief.append({
            "type": "image",
            "image": [
                mask_file, brain_file
            ],
            "viewer": "panelViewer"
        })



    response = {
        "id": job["id"],
        "success": True,
        "output": outputs,
        "report": [],
        "dataLog": log,
        "start": start,
        "brief": brief,
        "finish": str(datetime.now(tz=None))
    }

    pprint(response)

    rabbit_return(job, response)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        main(json.load(file))

