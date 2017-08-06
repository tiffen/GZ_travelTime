#合并几个文件成一个文件
import SelfValidMAPE
path = "C:\\Users\\NLSDE\\Desktop\\GZ_kdd\\result\\"
#进行selfValid时启用的代码
# path = "C:\\Users\\NLSDE\\Desktop\\GZ_kdd\\selfValid\\"
#找出数组中最小的非0元素
def findMinExceptZero(a):
    tmp = sorted(a)
    for i in tmp:
        if i != 0:
            return i
    return 0
def integer(file1,file2,file3,outputfile):
    result_dict_1={}
    result_dict_2={}
    result_dict_3={}
    with open(path+file1) as f1:
        all = f1.readlines()
        for i in range(len(all)):
            values = all[i].replace("\n","").split("#")
            result_dict_1[(values[0],values[1],values[2])] = float(values[3])
    with open(path+file2) as f2:
        all = f2.readlines()
        for i in range(len(all)):
            values = all[i].replace("\n","").split("#")
            result_dict_2[(values[0],values[1],values[2])] = float(values[3])
    with open(path+file3) as f3:
        all = f3.readlines()
        for i in range(len(all)):
            values = all[i].replace("\n","").split("#")
            result_dict_3[(values[0],values[1],values[2])] = float(values[3])
    with open(path+outputfile,"w") as f4:
        for i in result_dict_1:
            f4.write("#".join(i)+"#"+str(findMinExceptZero([result_dict_1[i],result_dict_2[i],result_dict_3[i]]))+"\n")
outputfile = "submit_SVRFcnmean5andknn_803.txt"
integer("submit_fcn_mean5.txt","knn_803.txt","SVR_rbfModel0802.txt",outputfile)
#下面是生成自验证的本地结果的代码
# 进行gridsearch找出最好的乘比例
# per_LVrange = [i/10 for i in range(10,20)]
# per_HVrange = [i/10 for i in range(10,15)]
# for perLV in per_LVrange:
#     for perHV in per_HVrange:
#         outputFile = "selfvalid_SVRAndfcnmean5AndKNN803LV_"+str(perLV)+"HV_"+str(perHV)+".txt"
#         integer("selfvalid_SVRAndfcnmean5AndKNN803.txt","selfvalid_historyValueByday_"+str(perHV)+".txt",
#                 "selfValid_lastValue_"+str(perLV)+".txt",outputFile)
#         SelfValidMAPE.processingOut(outputFile)
# outputFile = "selfvalid_SVRAndfcnmean803AndKNN803LV1.2HV1.0.txt"
# integer("selfvalid_SVRAndfcnmean803AndKNN803LV1.2.txt","selfvaild_fcn_mean803.txt",
#         "selfvalid_historyValueByday_1.0.txt",outputFile)
# SelfValidMAPE.processingOut(outputFile)
