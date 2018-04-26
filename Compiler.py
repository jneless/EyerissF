import numpy as np
import conf
import EyerissF


class Compiler:

    def __init__(self):
        pass

    def Con2LogicalMapping(self, Pictures, FilterWeights):
        # Call should be like :
        # '''Picture,FilterWeight=self.RawStationry(Pictures,FilterWeights)'''
        if len(Pictures) == 1:
            Picture, FilterWeight = self.FmapReuse(Pictures, FilterWeights)
        elif len(FilterWeights) == 1:
            Picture, FilterWeight = self.FilterReuse(Pictures, FilterWeights)
        else:
            Picture, FilterWeight = self.ChannelAccumulation(Pictures, FilterWeights)

        return Picture, FilterWeight

    def FmapReuse(self, Pictures, FilterWeights):

        assert len(Pictures) == 1

        NewArray = list()
        NewArrayLines = list()
        Picture = Pictures
        for x in range(0, len(FilterWeights[0])):
            # third, move the next pic NewArray
            for y in range(0, len(FilterWeights[0][0])):
                # second, in the same NewArray do the same operations
                for z in range(0, len(FilterWeights)):
                    # first, write different pics' pixs in a NewArray
                    NewArrayLines.append(FilterWeights[z][x][y])
            NewArray.append(np.hstack(NewArrayLines))
            NewArrayLines.clear()
        FilterWeight = np.array(NewArray)
        return Picture, FilterWeight

    def FilterReuse(self, Pictures, FilterWeights):

        assert len(FilterWeights) == 1

        FilterWeight = FilterWeights
        l = list()
        line = list()
        for y in range(0, len(Pictures[0])):
            # second move to next line to loop the inner operations
            for x in range(0, len(Pictures)):
                # first combine two lines ,which locate on different pics, to one line
                l.append(Pictures[x][y])
            line.append(np.hstack(l))
            l.clear()
        Picture = np.array(line)
        return Picture, FilterWeight

    def ChannelAccumulation(self, Pictures, FilterWeights):

        line = list()
        l = list()

        for x in range(0, len(Pictures[0])):
            for y in range(0, len(Pictures[0][0])):
                for z in range(0, len(Pictures)):
                    l.append(Pictures[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        Picture = np.array(line)
        line.clear()

        for x in range(0, len(FilterWeights[0])):
            for y in range(0, len(FilterWeights[0][0])):
                for z in range(0, len(FilterWeights)):
                    l.append(FilterWeights[z][x][y])
            line.append(np.hstack(l))
            l.clear()
        FilterWeight = np.array(line)
        line.clear()

        return Picture, FilterWeight

    def Con2PhysicalMapping(self,Picture, FilterWeight):

        x = 0
        t=list()
        while conf.EyerissWidth * x + conf.EyerissWidth + len(FilterWeight) -1 < len(FilterWeight) + len(Picture) -1:

            P=Picture[conf.EyerissWidth * x : conf.EyerissWidth * x + conf.EyerissWidth + len(FilterWeight) -1 ]
            x=x+1
            t.append(P)

        P=Picture[conf.EyerissWidth * x:]
        t.append(P)


        return t


if __name__=="__main__":
    cp=Compiler()

    # Pic=np.random.randint(-1,2,(100,2))
    # flt=np.random.randint(-1,2,(5,2))

    pic=np.ones((20,5),dtype=int)
    flt=np.ones((5,5),dtype=int)


    print(cp.Con2PhysicalMapping(pic,flt))

