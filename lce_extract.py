#pr plot 2 #for data measured by code
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import math
import pickle
# plt.rcParams.update({'font.size': 14})

lceDict = {
"Frank":{"measurements":
['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',
'lce_much_later',
'lce_reset',
'dup_original',
'lce_dyn_10p_dup',
'lce_dyn_20p_dup',
'lce_dyn_30p_dup',
'lce_dyn_40p_dup',
'reset_original',
'reset_10p',
'reset_20p',
'reset_40p',
'lce_dup_original',
'lce_dup_24hrs_10p',
'lce_dup_24hrs_20p',
'lce_dup_24hrs_30p',
'lce_dup_24hrs_40p',
'reset4_new_original',
'reset4_10p',
'reset4_20p',
'reset4_30p',
'reset4_40p',
'reset_1_22',
'expansion'
],
"compressions":[0,10,20,30,40,40,40,0,10,20,30,40,0,10,20,40,0,10,20,30,40,0,10,20,30,40,0,26],
"sample_types":['elastomer','elastomer_dyn','lce','lce_dyn'],},

"carrot":{"measurements":['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',],"compressions":[0,10,20,30,40],"sample_types":['elastomer','lce','lce_dyn']},

"broccoli":{"measurements":['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',],"compressions":[0,10,20,30,40],"sample_types":['elastomer','lce','lce_dyn']},

"garlic":{"measurements":['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',
'2layer_original',
'2layers_24hrs_30p',
'2layers_24hrs_40p'],"compressions":[0,10,20,30,40,0,30,40],"sample_types":['lce','lce_dyn']},

"queen":{"measurements":['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',],"compressions":[0,10,20,30,40],"sample_types":['lce','lce_dyn']},

"haricot":{"measurements":['originals',
'24hrs_10p',
'24hrs_20p',
'24hrs_30p',
'24hrs_40p',],"compressions":[0,10,20,30,40],"sample_types":['lce','lce_dyn']}
}

prDict = {}
# prDict["names"]={}
# prDict["names"]["samples"]={}
# prDict["names"]["samples"]["containers"]={}



for sample, detail in lceDict.items():
    prDict[sample]={}
    containers = detail["measurements"]
    compressions = detail["compressions"]
    samples = detail["sample_types"]

    #open saved measurements by gathering files
    for s in samples:
        prDict[sample][s]={}
        print(s)


        for i in range(len(containers)):
            files=[]
            container=containers[i]
            comp=compressions[i]
            src = '/media/savannah/My Book/lce_data/'+sample+'/'+container+'/pr_data'

            for file in os.listdir(src):
                if '.npy' in file:
                    if s in file:
                        if 'dyn' not in s:
                            if 'dyn'not in file:
                                filename=src+'/'+file
                                files.append(filename)
                        else:
                            filename=src+'/'+file
                            files.append(filename)
            print(files)
            #extract Poisson's ratios
            all_vals=[]
            for f in files:
                value=np.load(str(f),allow_pickle=True)
                num=value[1][value[2]]
                print(num)
                # plt.scatter(comp,num)
                all_vals.append(num)
            val=np.mean(all_vals)
            dev=np.std(all_vals)
            err=dev/len(all_vals)
            # plt.errorbar(comp,val,yerr=err/2,capsize=2)
            print(val)
            # plt.show()
            if math.isnan(val):
                print('Not available')
            else:
                prDict[sample][s][container] = {"avg_pr":round(val,3),"comp":comp,"error":err}





print(prDict)
outputPath ='/home/savannah/Desktop/Savannah/lce_code_data/'
with open(f"{outputPath}/prDict.pkl","wb") as f:
    pickle.dump(prDict,f,protocol=pickle.HIGHEST_PROTOCOL)


# for name in net_folds:
#     src = '/media/savannah/My Book/lce_data/'+name+'/'
#     prs=[]
#     comps=[]
#     for cat,compression in containers.items():
#         comps.append(compression)
#         for sample in sample_type:
#             files=[]
#             nw_src=src+cat+'/pr_data/'
#             for file in os.listdir(nw_src):
#                 if '.npy' in file:
#                     if sample in file:
#                         if 'dyn' not in sample:
#                             if 'dyn'not in file:
#                                 filename=nw_src+'/'+file
#                                 files.append(filename)
#                         else:
#                             filename=nw_src+'/'+file
#                             files.append(filename)
#             print(files)
#

# #process elastomer data:
# elastomer_prs=[]
# elastomer_dyn_prs=[]
# lce_prs=[]
# lce_dyn_prs=[]
# for comp in compressions:
#     print(comp)
#     abc_vals=[]
#     for f in elastomer_files:
#         if comp in f:
#             value=np.load(str(f),allow_pickle=True)
#             num=value[1][value[2]]
#             abc_vals.append(num)
#     value=np.mean(abc_vals)
#     elastomer_prs.append(value)
#     abc_vals=[]
#     for f in elastomer_dyn_files:
#         if comp in f:
#             value=np.load(str(f),allow_pickle=True)
#             num=value[1][value[2]]
#             abc_vals.append(num)
#     value=np.mean(abc_vals)
#     elastomer_dyn_prs.append(value)
#     abc_vals=[]
#     for f in lce_files:
#         if comp in f:
#             value=np.load(str(f),allow_pickle=True)
#             num=value[1][value[2]]
#             abc_vals.append(num)
#     value=np.mean(abc_vals)
#     lce_prs.append(value)
#     abc_vals=[]
#     print(lce_prs)
#     for f in lce_dyn_files:
#         if comp in f:
#             value=np.load(str(f),allow_pickle=True)
#             num=value[1][value[2]]
#             abc_vals.append(num)
#     value=np.mean(abc_vals)
#     lce_dyn_prs.append(value)
#
# # elastomer_prs=elastomer_prs[~np.isnan(elastomer_prs)]
# # elastomer_prs=np.array(elastomer_prs)[~np.isnan(elastomer_prs)]
# # elastomer_dyn_prs=np.array(elastomer_dyn_prs)[~np.isnan(elastomer_dyn_prs)]
#
# # elastomer_dyn_prs=elastomer_dyn_prs[~np.isnan(elastomer_dyn_prs)]
# # elastomer_dyn_prs=elastomer_dyn_prs[~np.isnan(elastomer_dyn_prs)]
# # lce_prs=lce_prs[~np.isnan(lce_prs)]
# lce_prs=np.array(lce_prs)[~np.isnan(lce_prs)]
# # lce_dyn_prs=np.array(lce_dyn_prs)[~np.isnan(lce_dyn_prs)]
#
# comp_vals=[0,10,20,30,40,0,10,20,40]
# # comp_vals_mod=[0,10,20,30,40,40,40]
# # comp_vals_dynmod=[0,10,20,30,40,0,10,20,30,40]
# print(lce_prs)
# # plt.scatter([0,10,20],elastomer_prs,color='b',label='elastomer')
# plt.scatter(comp_vals[:5],lce_prs[:5],color='navy',label='lce')
# plt.scatter(comp_vals[5:],lce_prs[5:],color='blue',label='lce_reset')
# # plt.scatter(comp_vals,lce_dyn_prs,color='maroon',label='lce_dyn')
# # plt.scatter(comp_vals[:-1],elastomer_dyn_prs,color='r',label='elastomer_dyn',marker='^')
# # plt.scatter(comp_vals_mod[:-2],lce_prs[:-2],color='navy',label='lce')
# # plt.scatter(comp_vals_dynmod,lce_dyn_prs,color='maroon',label='lce_dyn',marker='^')
# # plt.scatter(comp_vals_mod,lce_prs,color='navy',label='lce')
#
# # plt.scatter(comp_vals_mod[-2],lce_prs[-2],color='#bfcfff',label='lce later',edgecolors='navy')
# # plt.scatter(comp_vals_mod[-1],lce_prs[-1],color='#809fff',label='lce reset',edgecolors='navy')
# # plt.scatter(comp_vals_dynmod[-5:],lce_dyn_prs[-5:],color='maroon',label='lce_dyn_dup',marker='^',edgecolors='pink')
#
#
# plt.ylim(-0.6,0.8)
#
# locs,labels = plt.xticks()
#
# newlabels = []
# new_locs=[]
# for il in range(len(locs)):
#     loc = locs[il]
#     print(loc)
#     if il % 2 == 1:
#         newlabels.append(int(loc))
#         new_locs.append(loc)
#
# plt.xticks(new_locs,newlabels)
# plt.ylabel(r'$\nu$')
# plt.xlabel('Compression (%)')
# plt.legend()
# # plt.savefig('/media/savannah/My Book/lce_data/'+net_fold+'/pr_v_compression_update_11_12.pdf',dpi=300)
# # plt.savefig('/media/savannah/My Book/lce_data/'+net_fold+'/pr_v_compression_broccoli_data.pdf',dpi=300)
# plt.show()


# #find image files
# net_fold="Frank"
# # net_fold="Frank"
# src = '/media/savannah/My Book/lce_data/'+net_fold+'/'+fold+'/'+sample+'/'+letter+'/'
# print(src)
# # src = '/media/savannah/My Book/Materials/2024_8_6/'+net_fold+'/'+fold+'/'+sample+'/'
# mov=[]

# plt.savefig('/media/savannah/My Book/lce_data/'+net_fold+'/'+fold+'/pr_data/'+str(sample)+'_'+letter+'_pr_l.png',dpi=300)
# plt.show()
# np.save('/media/savannah/My Book/lce_data/'+net_fold+'/'+fold+'/pr_data/'+str(sample)+'_'+letter+'_pr.npy',[ls[1:]/ls[0],pr,spot])
# plt.figure()
# plt.scatter(fr[1:],pr)
# plt.ylim(-0.6,1.0)
# plt.savefig('/media/savannah/My Book/lce_data/'+net_fold+'/'+fold+'/pr_data/'+str(sample)+'_'+letter+'_pr_t.png',dpi=300)
# plt.show()

#import first trial data:
# samples=['paul','queen','rick','sabrina']
# samples=['elastomer','elastomer_catalyst','lce_nd','lce']
# samples=['elastomer_day2','elastomer_catalyst_day2','lce_nd_day2','lce_day2']
# # samples=['elastomer_day3','elastomer_catalyst_day3','lce_nd_day3','lce_day3']
# colors=['red','blue','green','purple']
# for i in range(4):
#     sample=samples[i]
#     color=colors[i]
#     # l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_original_prdata.npy',allow_pickle=True)
#     # l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_original_prdata.npy',allow_pickle=True)
#     l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_prdata.npy',allow_pickle=True)
#     original=pr[spt]
#     plt.scatter(0,original,color=color)
#     # al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_aged_prdata.npy',allow_pickle=True)
#     # aged=apr[aspt]
#     # plt.scatter(6,aged,color=color)
#
# # plt.savefig('/home/savannah/Desktop/4_16_24/continuous_age_p_s.png',dpi=300)
# # plt.ylim(-0.5,0.8)
# # plt.show()
#
# # trial 2
# # samples=['paul2','queen2','rick2','sabrina2']
# # samples=['elastomer','elastomer_catalyst','lce_nd','lce']
# samples=['elastomer_age3hrs','elastomer_catalyst_age3hrs','lce_nd_age3hrs','lce_age3hrs']
# # samples=['elastomer_d3_3hrs','elastomer_catalyst_d3_3hrs','lce_nd_d3_3hrs','lce_d3_3hrs']
# colors=['red','blue','green','purple']
# # nums=['1hr','2hrs','3hrs']
# nums=['1hr','2hrs']
# for i in range(4):
#     sample=samples[i]
#     color=colors[i]
#     # l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_original_prdata.npy',allow_pickle=True)
#     # original=pr[spt]
#     # plt.scatter(0,original,color=color,marker='x')
#     # for num in nums:
#     # al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_'+num+'_prdata.npy',allow_pickle=True)
#     al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_prdata.npy',allow_pickle=True)
#     aged=apr[aspt]
#     # plt.scatter(int(num[0]),aged,color=color,marker='x')
#     # plt.scatter(int(num[0]),aged,color=color)
#     plt.scatter(3,aged,color=color)
# plt.ylim(-0.5,0.7)
# plt.savefig('/home/savannah/Desktop/4_16_24/lce_3hr_age.png',dpi=300)
#
# plt.show()

# # trial 3
# samples=['elastomer_3hrs_stretch','elastomer_catalyst_3hrs_stretch','lce_nd_3hrs_stretch','lce_3hrs_stretch']
# colors=['red','blue','green','purple']
# # nums=['1hr','2hrs','3hrs']
# nums=['1hr','2hrs']
# for i in range(4):
#     sample=samples[i]
#     color=colors[i]
#     # l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_original_prdata.npy',allow_pickle=True)
#     # original=pr[spt]
#     # plt.scatter(0,original,color=color,marker='x')
#     # for num in nums:
#     # al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_'+num+'_prdata.npy',allow_pickle=True)
#     al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_prdata.npy',allow_pickle=True)
#     aged=apr[aspt]
#     # plt.scatter(int(num[0]),aged,color=color,marker='x')
#     # plt.scatter(int(num[0]),aged,color=color)
#     plt.scatter(3.5,aged,color=color)
# plt.ylim(-0.5,0.7)
# plt.savefig('/home/savannah/Desktop/4_16_24/lce_age_stretch.png',dpi=300)
#
# plt.show()
# # #trial 3
# # samples=['paul3','queen3','rick3','sabrina3']
# # colors=['red','blue','green','purple']
# # nums=['age30m','1hr','1.5hrs','2hrs','2.5hrs']
# # ts=[.5,1,1.5,2,2.5]
# # for i in range(4):
# #     sample=samples[i]
# #     color=colors[i]
# #     l,pr,spt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_original_prdata.npy',allow_pickle=True)
# #     original=pr[spt]
# #     plt.scatter(0,original,color=color,marker='^')
# #     for j in range(len(nums)):
# #         num=nums[j]
# #         al,apr,aspt=np.load('/home/savannah/Desktop/pr_measures/numbers/'+sample+'_'+num+'_prdata.npy',allow_pickle=True)
# #         aged=apr[aspt]
# #         plt.scatter(ts[j],aged,color=color,marker='^')
# plt.ylim(-0.5,0.7)
# plt.savefig('/home/savannah/Desktop/4_16_24/age_lces.png',dpi=300)
#
# plt.show()
# # # x=[0,3,6,9,12,17]
# x=[0,1,2,3,4,5]
# # x=[0,1,2,3,4]
# lce=[o,lce_3,lce_6,lce_9,lce_12,-0.192]
# # lce=[o,lce_3,lce_6,lce_9,lce_12]
#
# # rx=[3,6,9]
# rx=[1,2,3]
# rest=[r_3,r_6,r_9]
#
# # xmod=[0,3,6,9]
# xmod=[0,1,2,3]
# rest_mod=[o,r_3,r_6,r_9]
#
# #connect rested and cycled points
# x_mod=[0,1,1,2,2,3,3,4,5]
# lce_mod=[o,lce_3,r_3,lce_6,r_6,lce_9,r_9,lce_12,-0.192]
#
# # plt.plot(fm_x,fm,color='gray',zorder=1)
# # plt.scatter(fm_x,fm,color='gray',edgecolor='black',s=55,label='Foam',zorder=2)
# # plt.plot(x,lce, color='#f5d142',zorder=1)
# plt.scatter(x,lce, color='#f5d142',edgecolor='black',s=55,Label='LCE',zorder=2)
# plt.plot(x_mod,lce_mod, color='black',zorder=1)
# plt.scatter(rx,rest, color='#f5d142',edgecolor='black',s=55,marker='^',zorder=2,label='Rest 24hrs')
#
#
# plt.hlines(0,0,5.5,color='gray',linestyle='--')
#
#
# plt.xlim(-.1,5.5)
# plt.ylim(-0.4,0.4)
#
# # locs,labels = plt.xticks([0,3,6,9,12,15,18],[0,3,6,9,12,15,18])
#
# locs,labels = plt.yticks()
# print(locs)
# newlabels = []
# for il in range(len(locs)):
#     loc = locs[il]
#     print(loc)
#     if il % 2 == 0:
#         newlabels.append(str(round(loc,3)))
#     else:
#         newlabels.append("")
# plt.yticks(locs,newlabels)
#
# plt.legend()
# plt.savefig('/home/savannah/Desktop/March_meeting_2024/rested_prdat_mod.png',dpi=300)
# plt.show()
