
pc1_max = max(finalDf['principal component 1'])
pc1_min = min(finalDf['principal component 1'])
pc2_max = max(finalDf['principal component 2'])
pc2_min = min(finalDf['principal component 2'])

pca_plot = plt.scatter(finalDf['principal component 1'], finalDf['principal component 2'],
                      s = 10, c = finalDf['y'], cmap='viridis')
plt.title("CASP - PCA Plot of Testset: PC1 vs. PC2", fontsize=15)
plt.xlabel("PC1", fontsize=14)
plt.ylabel("PC2", fontsize=14)
# plt.xticks(fontsize=20, rotation=90)
plt.xticks(fontsize=11)   # Set font size for better visualization
plt.yticks(fontsize=11)
plt.xlim(pc1_min, pc1_max)
plt.ylim(pc2_min, pc2_max)

cbar = plt.colorbar()
for t in cbar.ax.get_yticklabels():
     t.set_fontsize(13)
plt.savefig('pca_casp.jpg')
plt.show()




    plt.imshow(diff_predictions_np.transpose().tolist(), cmap = plt.get_cmap('seismic'), 
               clim=(elev_min, elev_max), norm=MidpointNormalize(midpoint=mid_val,vmin=elev_min, vmax=elev_max))
    cbar = plt.colorbar()
    for t in cbar.ax.get_yticklabels():
         t.set_fontsize(14)
    plt.xticks(range(0,15), labels = range(1,16), fontsize = 10)
    plt.yticks(range(0,20), labels = range(1,21), fontsize = 10)
    plt.title("Pred: curr. model vs. original model ("+ method+")", fontsize=15)
    plt.xlabel("Query Batches", fontsize=15)
    plt.ylabel("Test Sample Indices", fontsize=15)
    plt.savefig("change_query_plot_original_" + method +".jpg")
    plt.show()