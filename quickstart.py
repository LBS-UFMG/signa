import Signa.signa as signa
# from signa import signa  #instalação local do signa v0.2 => /opt/homebrew/lib/python3.9/site-packages/signa

# help(signa)  # for obtaining more details use this command
# print(signa.version)  # returns signa version

entry = './docs/examples/as.pdb'
signature = ''

# Simple use
#signature = signa.read(entry, 'acsm-all', cutoff_limit=10, cutoff_step=0.1, separator=",", cumulative=True)

# SIGNA-CHARGE
#signature = signa.read(entry, signa_type='SIGNA-CHARGE', forcefield="AMBER", cutoff_limit=12, cutoff_step=1.0, cumulative=False)

# signature = signa.read(entry, 'csm', cutoff_limit=30, cutoff_step=0.2, separator=",", cumulative=True)

# Obtaining the labels
labels_example = signa.labels(signa_type='acsm-all', cutoff_step=0.05, cutoff_limit=6, separator=",", cumulative=True)
print(labels_example)
# exit()

# signature = signa.read(entry, 'acsm')

# signature = signa.read(entry, 'acsm_hp')

# signature = signa.read(entry, 'acsm_all')

# Select a specific chain
# signature = signa.read(entry, 'csm', chain='A')

# Multiple files - CSV
# signa.read_csv(
#  	csv_file='./docs/case_studies/cs4/input_cs4.csv', 
#  	signa_type='acsm-all', 
#     cumulative=True,
#    #  forcefield='AMBER',
#  	output='./docs/case_studies/cs4/output_acsm.csv',
#     cutoff_limit=20
# )

# Multiple files - Folder
# signa.read_folder(
#  	folder='./docs/case_studies/cs7/interfaces', 
#  	signa_type='acsm-all', 
#     cumulative=True,
#  	output='./docs/case_studies/cs7/output_acsm_nc_2.csv',
#     cutoff_limit=6,
#     cutoff_step=0.05,
#     format='pdb'
# )

# SSV - Comparisons between signatures
#ssv = signa.ssv(entry, entry)
#print(ssv)
# signature = signa.read("./docs/case_studies/cs4/pdb/AAGAATTAAGAASGA.pdb", 'signa-charge', forcefield='AMBER',cutoff_limit=12, cutoff_step=0.2, separator=",", cumulative=True)

print(signature)