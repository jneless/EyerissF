import Hive
import EyerissF as Eyeriss

eyeriss = Eyeriss()
hive=Hive.Hive(eyeriss,Operation="handmade")

Pictures=[]
FilterWeights=[]


############################################################


hive.input(Pictures,FilterWeights)  # DRAM to Hive DRAM
hive.Conv2LogicalMapping() # DRAM
hive.Conv2PhyscialMapping() # DRAM
hive.Conv2d() # return Compressed-Pics

Pictures=hive.GetOutput()
Pictures = hive.GetOutput()


############################################################

Pictures = hive.Pooling() # Compressed-Pics Pool to Compressed-Pics

############################################################








