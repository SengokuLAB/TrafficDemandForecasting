import os 

class Path:
    def __init__(self):
        ## paths
        self.path_1 = r"C:\\Users\\impor\\Documents\\SengokuLab\\private\\transportation\\data\\dev\\"
        self.path_2 = r"..\\..\\data\\dev\\"

        # select path
        if os.path.exists(self.path_1):
            self.path = self.path_1
        elif os.path.exists(self.path_2):
            self.path = self.path_2
        else:
            self.path = str()
            

    def get_od(self):
        path_od = "02_分布交通量\\OD.csv" # path of od data
        return self.path + path_od

    def get_linknode(self):
        path_linknode = "03_配分交通量\\LinkNode.csv" # path of linknode data
        return self.path + path_linknode

    def get_coeff(self):
        path_coeff = "03_配分交通量\\coeff.csv" # path of linknode data
        return self.path + path_coeff

    def get_savefile(self):
        today = re.sub(r'-',"",str(datetime.date.today())).lstrip("20")#今日の日付
        path_savefile = "Assignment\\%s"%(today,) # path of save file
        if not os.path.exists(self.path + path_savefile):
            os.mkdir(self.path + path_savefile)
        return self.path + path_savefile
