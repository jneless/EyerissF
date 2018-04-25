import numpy as np
import conf
import EyerissF


class Compiler:

    def __init__(self):
        pass

    def RawStationry(self, Pictures, FilterWeights):
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
