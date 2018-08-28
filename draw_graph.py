x=[u'0.0~0.1',u'0.1~0.2',u'0.2~0.3',u'0.3~0.4',u'0.4~0.5',u'0.5~0.6',u'0.6~0.7',u'0.7~0.8',u'0.8~0.9',u'0.9~1.0']
spammer=[s_group1,s_group2,s_group3,s_group4,s_group5,s_group6,s_group7,s_group8,s_group9,s_group10]
nonspammer=[n_group1,n_group2,n_group3,n_group4,n_group5,n_group6,n_group7,n_group8,n_group9,n_group10]

plt.plot(x,spammer,color='red',marker='o',linestyle='solid')
plt.plot(x,nonspammer,color='blue',marker='o',linestyle='solid')
#labels=spammer

plt.title('max of review similarity')
plt.xlabel("similarity")
plt.ylabel("number of reviewer(%)")
plt.xticks(np.arange(len(x)),x,rotation=45)

'''
for label, x_count, y_count in zip(labels, x, spammer):
    plt.annotate(label,
                 xy=(x_count, y_count), #label을 데이터포인트에 두되
                 xytext=(3,-9), # 약간 떨어져 있게
                 textcoords='offset points')
'''

plt.savefig("graph.png", bbox_inches="tight")
plt.show()

