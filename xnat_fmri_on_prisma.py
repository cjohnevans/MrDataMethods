import xnatproc

fname = 'sapje1_2_17_2022_11_26_25.csv'
#scanfilter = {'Project': '417_mrlabdev', 'Scanner': 'AWP66073'}
scanfilters = [{'Scanner': '66073', 'Scans': 'bold'}, \
               {'Scanner': '66073', 'Scans': 'fmri'}, \
               {'Scanner': '66073', 'Scans': 'mb'}, \
               {'Scanner': '66073', 'Scans': 'ep2d'} \
               ]

scans = xnatproc.XnatProc()
scans.read_scan_list(fname)

allfmri = []
for flt in scanfilters:
    this_flt = scans.filter_scan_list(flt)
    print('flt', flt, 'this_flt', len(this_flt))
    allfmri = allfmri + this_flt
    print('allfmri', len(allfmri))

proj_list = []
[ proj_list.append(idx['Project']) for idx in allfmri ]
proj_list.sort()
proj_unique  = set(proj_list)
proj_unique = list(proj_unique)
proj_unique.sort()
[ print(pj) for pj in proj_unique ]

