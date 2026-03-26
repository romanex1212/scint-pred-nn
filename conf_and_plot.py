import numpy as np
import matplotlib.pyplot as plt
import itertools

class confusion_matrix_plots:
    def __init__(self, true, pred):
        self.true = true
        self.pred = pred

    # Function to calculate the confusion matrix entries
    def confusion_table(self):
        """
        computes the number of TP, TN, FP, FN events given the arrays with observations and predictions
        and returns the true skill score
    
        Args:
        true: np array with observations (1 for scintillation, 0 for nonscintillation)
        pred: np array with predictions (1 for scintillation, 0 for nonscintillation)
    
        Returns: true negative, false positive, true positive, false negative
        """  
        Nobs = len(self.pred)
        TN = 0.; TP = 0.; FP = 0.; FN = 0.
        for i in range(Nobs):
            if (self.pred[i] == 0 and self.true[i] == 0):
                TN += 1
            elif (self.pred[i] == 1 and self.true[i] == 0):
                FP += 1
            elif (self.pred[i] == 1 and self.true[i] == 1):
                TP += 1 
            elif (self.pred[i] == 0 and self.true[i] == 1):
                FN += 1
            else:
                print("Error! Observation could not be classified.")
        return TN,FP,TP,FN

    # Function to plot the confusion matrix
    def plot_confusion_matrix(self, cm, classes,
                            normalize=False,
                            title='Confusion matrix',
                            cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """

        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        cb = plt.colorbar()
        cb.ax.tick_params(labelsize=20) 
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)#,fontsize=22, weight='bold')
        plt.yticks(tick_marks, classes)#,fontsize=22, weight='bold')

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black",fontsize=22, weight='bold')

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')