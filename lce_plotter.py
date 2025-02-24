#pr plot 2 #for data measured by code
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
import os
import pickle
import pandas as pd

plt.rcParams.update({'font.size': 11})
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)


#open file with data
inputPath ='/home/savannah/Desktop/Savannah/lce_code_data/'
with open(f"{inputPath}/prDict.pkl","rb") as f:
    prDict=pickle.load(f)

net_folds=[
"Frank",
"carrot",
"broccoli",
"garlic",
"queen"
]
containers=[
'originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',
# 'lce_much_later',
# 'lce_reset',
# 'dup_original',
# 'lce_dyn_10p_dup',
# 'lce_dyn_20p_dup',
# 'lce_dyn_30p_dup',
# 'lce_dyn_40p_dup',
# 'reset_original',
# 'reset_10p',
# 'reset_20p',
# 'reset_40p',
]


sample_type=[
# 'elastomer',
# 'elastomer_dyn',
'lce',
# 'lce_dyn'
]

# figure 1
plt.rcParams["figure.figsize"] = (3.4,2.7)

net_folds=[
"Frank",
"carrot",
"broccoli",
"garlic",
"queen",
"haricot"
]
containers=[
'originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',]
sample_type=[
'lce',
#'elastomer'
]
additional_containers=[
'lce_dup_original',
'lce_dup_24hrs_10p',
'lce_dup_24hrs_20p',
'lce_dup_24hrs_30p',
'lce_dup_24hrs_40p'
]

colors=["#173f62","#5b8f99","#faab5c","#bf3414","#851826","#ab4c03",]
symbols=["o","^","s","*",">","x","P"]
ms_list=[30,30,30,40,30,30,30]
# nets=['1','2','3','4','5']
for i in range(len(net_folds)):
    name=net_folds[i]
    s=symbols[i]
    ms=ms_list[i]
    # g=grays[i]
    color=colors[i]
    # net=nets[i]
    # for sample in sample_type:
    sample='lce'
    pr_list=[]
    comps_list=[]
    for c in containers:
        pr=prDict[name][sample][c]["avg_pr"]
        scale_pr=prDict[name][sample]["originals"]["avg_pr"]
        comp=prDict[name][sample][c]["comp"]
        err=prDict[name][sample][c]["error"]
        plt.scatter(comp,pr,color=color,marker=s,s=ms)
        pr_list.append(pr)
        comps_list.append(comp)
        # plt.errorbar(comp,pr,yerr=.08/2,color=color,capsize=2)
    plt.plot(comps_list,pr_list,color=color,zorder=1)
    if "Frank" in name:
        for sample in sample_type:
            pr_list=[]
            comps_list=[]
            for c in additional_containers:
                pr=prDict[name][sample][c]["avg_pr"]
                scale_pr=prDict[name][sample]["originals"]["avg_pr"]
                comp=prDict[name][sample][c]["comp"]
                err=prDict[name][sample][c]["error"]
                plt.scatter(comp,pr,color=color,marker=symbols[-1],s=ms)
                plt.errorbar(comp,pr,yerr=err/2,color=color,capsize=2)
                pr_list.append(pr)
                comps_list.append(comp)
            plt.plot(comps_list,pr_list,color=color,zorder=1)
plt.ylim(-0.6,0.8)
plt.xlim(-1,42)

locs,labels = plt.yticks()
newlabels = []
new_locs=[]
for il in range(len(locs)):
    loc = locs[il]

    if il % 2 == 1:
        newlabels.append(round(loc,2))
        # new_locs.append(loc)
    else:
        newlabels.append("")

plt.yticks(locs,newlabels)
plt.axhline(0,-1,42,color='lightgray',linestyle='--', linewidth=1,zorder=0)
plt.ylabel(r'$\nu$')
plt.xlabel('Aging Compression (%)')
plt.tight_layout(pad=.05)
# plt.legend()
# plt.savefig('/media/savannah/My Book/lce_data/figures/pr_v_compression_all_networks_1_23.pdf',dpi=300)
plt.show()

#Figure 2:\
# plt.rcParams["figure.figsize"] = (3.375,2.5) #with labels
# # plt.rcParams["figure.figsize"] = (1.15,.85) #with labels
# net_folds=[
# "Frank",
# # "carrot",
# # "broccoli"
# ]
# containers=[
# 'originals',
# '24hrs_10p',
# '24hrs_20p',
# '24hrs_30p',
# '24hrs_40p',]
# sample_type=[
# 'elastomer',
# # 'elastomer_dyn',
# 'lce',
# # 'lce_dyn'
# ]
# alt_containers=[
# 'dup_original',
# 'lce_dyn_10p_dup',
# 'lce_dyn_20p_dup',
# 'lce_dyn_30p_dup',
# 'lce_dyn_40p_dup',
# ]
#
# colors=['r','b','g','black']
# # colors=["#173f62","#5b8f99","#faab5c","#bf3414","#851826"]
# colors=["#173f62","#faab5c","#bf3414","#851826"]
# # symbols=["o","o","^","^",">"]
# # symbols=["o","o","^","^"]
# symbols=["o","^","^"]
# labels=["elastomer","elastomer + catalyst","LCE","LCE + catalyst"]
# for j in range(len(net_folds)):
#     name=net_folds[j]
#     # color=colors[j]
#     # sym=symbols[j]
#
#     print(name)
#     for i in range(len(sample_type)):
#         sample=sample_type[i]
#         sym=symbols[i]
#         color=colors[i]
#         lab=labels[i]
#         pr_list=[]
#         comps_list=[]
#         if "Frank"in name and 'lce_dyn' in sample:
#                 for c in alt_containers:
#                     pr=prDict[name][sample][c]["avg_pr"]
#                     comp=prDict[name][sample][c]["comp"]
#                     err=prDict[name][sample][c]["error"]
#                     pr_list.append(pr)
#                     comps_list.append(comp)
#
#                     if 'original'in c:
#                         plt.scatter(comp,pr,color=color, label=lab,marker=sym)
#                         # plt.errorbar(comp,pr,yerr=err/2,color=color,capsize=2)
#                     else:
#                         plt.scatter(comp,pr,color=color,marker=sym)
#
#                         # plt.errorbar(comp,pr,yerr=err/2,color=color,capsize=2)
#         else:
#             os=[]
#             for c in containers:
#                 try:
#                     if c in prDict[name][sample]:
#                         pr=prDict[name][sample][c]["avg_pr"]
#                         comp=prDict[name][sample][c]["comp"]
#                         pr_list.append(pr)
#                         comps_list.append(comp)
#                         # err=prDict[name][sample][c]["error"]
#                         if 'originals'in c:
#                             os.append(pr)
#                             plt.scatter(comp,pr,color=color, label=lab,marker=sym)
#                             # plt.errorbar(comp,pr,yerr=err/2,color=color,capsize=2)
#
#                         else:
#                             print(name,comp,pr)
#                             plt.scatter(comp,pr,color=color,marker=sym)
#                             # plt.errorbar(comp,pr,yerr=err/2,color=color,capsize=2)
#                 except:
#                     print("no such file")
#         plt.plot(comps_list,pr_list,color=color,zorder=1)
# plt.ylim(-0.6,0.4)
# # plt.ylim(-0.55,1.1)
# plt.xlim(-1,42)
#
# locs,labels = plt.yticks()
#
# newlabels = []
# new_locs=[]
# for il in range(len(locs)):
#     loc = locs[il]
#     # print(loc)
#     if il % 2 == 1:
#         newlabels.append(round(loc,2))
#     else:
#         newlabels.append("")
#
# plt.yticks(locs,newlabels)
# plt.ylabel(r'$\nu$')
# plt.xlabel('Compression (%)')
# # plt.legend()
# plt.tight_layout(pad=.2)
# plt.savefig('/media/savannah/My Book/lce_data/figures/pr_v_compression_diff_samples_1_29_b.pdf',dpi=300)
# plt.show()

#figure 3
# plt.rcParams["figure.figsize"] = (3.375,2.5) #with labels
# net_folds=[
# "Frank",
# ]
# containers=[
# 'originals',
# '24hrs_10p',
# '24hrs_20p',
# '24hrs_30p',
# '24hrs_40p',
# 'reset_original',
# 'reset_10p',
# 'reset_20p',
# 'reset_40p',
# 'reset4_new_original',
# 'reset4_10p',
# 'reset4_20p',
# 'reset4_30p',
# 'reset4_40p',
# 'reset_1_22',
# 'expansion',
# ]
# sample_type=[
# 'lce'
# ]
# colors=["#173f62","#5b8f99","#faab5c","#bf3414","#851826","#ab4c03",]
# symbols=["o","^","P","*",">","x","P"]
# for name in net_folds:
#     for sample in sample_type:
#         pr_list=[]
#         comps_list=[]
#         for i in range(len(containers)):
#             c=containers[i]
#             pr=prDict[name][sample][c]["avg_pr"]
#             scale_pr=prDict[name][sample]["originals"]["avg_pr"]
#             comp=prDict[name][sample][c]["comp"]
#             # err=prDict[name][sample][c]["error"]
#             pr_list.append(pr)
#             comps_list.append(comp)
#             if i < 5:
#                 color="#173f62"
#                 if 'originals'in c:
#                     plt.scatter(comp,pr,color="#173f62",marker="o", label='original',s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#173f62",capsize=2)
#                 else:
#                     plt.scatter(comp,pr,color="#173f62",marker="o",s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#173f62",capsize=2)
#
#             elif i<9:
#                 color="#bf3414"
#                 if 'original'in c:
#                     plt.scatter(comp,pr,color="#bf3414", marker="^", label='reset 1',s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#bf3414",capsize=2)
#                 else:
#                     plt.scatter(comp,pr,color="#bf3414", marker="^",s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#bf3414",capsize=2)
#             elif i<14:
#                 color="#faab5c"
#                 if 'original'in c:
#                     plt.scatter(comp,pr,color="#faab5c",marker="P", label='reset 2',s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#faab5c",capsize=2)
#                 else:
#                     plt.scatter(comp,pr,color="#faab5c",marker="P",s=30)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#faab5c",capsize=2)
#             else:
#                 color="#851826"
#                 if 'reset'in c:
#                     plt.scatter(comp,pr,color="#ab4c03",marker="*", label='expansion',s=40)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#faab5c",capsize=2)
#                 else:
#                     plt.scatter(comp,pr,color="#ab4c03",marker="*",s=40)
#                     # plt.errorbar(comp,pr,yerr=err/2,color="#faab5c",capsize=2)
#         plt.plot(comps_list[:5],pr_list[:5],color="#173f62",zorder=1)
#         plt.plot(comps_list[5:9],pr_list[5:9],color="#bf3414",zorder=1)
#         plt.plot(comps_list[9:14],pr_list[9:14],color="#faab5c",zorder=1)
#         plt.plot(comps_list[14:],pr_list[14:],color="#ab4c03",zorder=1)
# plt.ylim(-0.6,0.6)
# plt.axhline(0,-1,42,color='lightgray',linestyle='--', linewidth=1,zorder=0)
# locs,labels = plt.xticks()
#
# #ylabels:
# locs,labels = plt.yticks()
# newlabelsy = []
# new_locsy=[]
# for il in range(len(locs)):
#     loc = locs[il]
#     if il ==0 or il==3 or il==6:
#         newlabelsy.append(round(loc,2))
#     else:
#         newlabelsy.append("")
#
# plt.yticks(locs,newlabelsy)
# # plt.xticks(new_locs,newlabels)
# plt.ylabel(r'$\nu$')
# plt.xlabel('strain (%)')
# # plt.legend()
# plt.tight_layout(pad=0.2)
# plt.savefig('/media/savannah/My Book/lce_data/figures/pr_v_compression_lce_reset_1_25.pdf',dpi=300)
# plt.show()

#figure 4
# plt.rcParams["figure.figsize"] = (3.375,2.5) #with labels
# plt.rcParams["figure.figsize"] = (2.5,2) #with labels
plt.rcParams["figure.figsize"] = (3,2.2) #with labels
colors=["#173f62","#faab5c","#5b8f99","#bf3414","#851826"]
symbols=["o","^","^","^",">"]
source_strains=[]
target_strains=[]
colz=["B:R",
#"S:Z",
"AO:AX"
]
for j in range(len(colz)):
    sym=symbols[j]
    cols=colz[j]
    data=pd.read_excel(r'/home/savannah/Documents/lce_allostery.ods','Sheet1',usecols=cols)

    #extract data

    df_labels=data[1:2].to_numpy()[0]
    df=data[2:4].to_numpy()
    print(df)

    #compute offset do to actuator:
    #get data without
    spots=np.where(df_labels=="no_act")[0]
    no_act_dat_src=df[:,spots]
    #original data with actuator
    o_spots=spots+1
    with_act_dat_src=df[:,o_spots]
    correction=(no_act_dat_src-with_act_dat_src[0])[0]
    print(spots)


    for i in range(len(o_spots)):
        start=o_spots[i]
        # c=colors[i]
        # s=symbols[i]
        if i==len(o_spots)-1:
            c=colors[1]
            all_dat=df[:,start:]
            nw_source=all_dat[0]+correction[0]
            trg_dat=all_dat[1]
            source_strain=(nw_source-nw_source[0])/nw_source[0]
            target_strain=(trg_dat-trg_dat[0])/trg_dat[0]
            source_strain=source_strain[1:]
            target_strain=target_strain[1:]
            plt.scatter(abs(source_strain),abs(target_strain),color=c,label="aged",marker=sym)
            # plt.scatter(source_strain,target_strain,color=c)

        elif i==0:
            c=colors[i]
            all_dat=df[:,start:spots[i+1]]
            nw_source=all_dat[0]+correction[i]
            trg_dat=all_dat[1]
            source_strain=(nw_source-nw_source[0])/nw_source[0]
            target_strain=(trg_dat-trg_dat[0])/trg_dat[0]
            source_strain=source_strain[1:]
            target_strain=target_strain[1:]
            plt.scatter(abs(source_strain),abs(target_strain),color=c,label="original",marker=sym)
            # plt.scatter(source_strain,target_strain,color=c)

plt.xlim(0,0.65)
plt.ylim(-.01,.2)
# locs,labels = plt.yticks()
# print(locs)
# newlabels = []
# # new_locs=[]
# for il in range(1,len(locs)):
#     loc = locs[il]
#     print(loc)
#     if il % 2 == 0:
#         newlabels.append(round(loc,2))
#         # new_locs.append(loc)
#     else:
#         newlabels.append("")
#
# plt.yticks(locs[1:],newlabels)

# plt.xlabel('|Source Strain|')
# plt.ylabel('|Target Strain|')
# plt.title("Local Coupling")
plt.tight_layout(pad=0.2)
# plt.legend()
plt.savefig('/media/savannah/My Book/lce_data/figures/allostery_1_29.pdf',dpi=300)
plt.show()
