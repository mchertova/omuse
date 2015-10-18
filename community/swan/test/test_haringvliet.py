import numpy

from omuse.community.swan.interface import SwanInterface

from matplotlib import pyplot

from amuse.test.amusetest import TestWithMPI

def read_bot_data(filename="f31hari.bot",n=117,m=88):
  f=open(filename,"r")
  lines=f.readlines()
  f.close()
  
  dat=[]
  for line in lines:
    for s in line.split():
      dat.append(float(s))
  
  return numpy.array(dat).reshape((n,m))

class TestHaringvliet(TestWithMPI):
    def test1(self):
      bathimetry=read_bot_data()


if __name__=="__main__":
  bathimetry=read_bot_data()

  pyplot.ion()
  f=pyplot.figure(figsize=(8,6))
  pyplot.show()
  pyplot.imshow(numpy.transpose(bathimetry),origin="lower")
  
  s=SwanInterface(redirection="none")
  
  print s.get_coordinates()
  print s.get_projection_method()
  print s.get_grid_type()
  print s.get_input_grid_type()
  print s.get_calc_mode()
  print s.get_number_dimensions()
  
  print s.initialize_code()
  
  s.set_wlev(0.3)
  wlev,err=s.get_wlev()
  
  s.set_grid_xpc(6960.2)
  s.set_grid_ypc(0.)
  s.set_grid_alpc(0.)
  s.set_grid_xlenc(14789.8)
  s.set_grid_ylenc(22000.)
  s.set_grid_mxc(98)
  s.set_grid_myc(88)

  s.set_nfreq(32)
  s.set_flow(0.0521)
  s.set_fhigh(1.)
  s.set_mdc(36)

  print s.get_nfreq()
  print s.get_flow()
  print s.get_fhigh()
  print s.get_mdc()

  s.set_input_xp(0.)
  s.set_input_yp(0.)
  s.set_input_alp(0.)
  s.set_input_dx(250.)
  s.set_input_dy(250.)
  s.set_input_mx(87)
  s.set_input_my(116)

  print s.initialize_grids()
  print s.commit_grids()
  print s.commit_parameters()
 
  print s.get_exc_value(1)
  
  input_shape=bathimetry.shape
  ii,jj=numpy.mgrid[1:input_shape[0]+1,1:input_shape[1]+1]
  print s.set_depth(ii.flatten(),jj.flatten(),bathimetry.flatten())

  print s.set_uniform_wind_vel(12.)
  print s.set_uniform_wind_dir(8.8)

  s.set_north_boundary_spec_file("f31har01.bnd")

  s.set_use_gen3(True)
  s.set_use_breaking(True)
  s.set_use_triads(True)
  s.set_use_friction(True)

  print s.initialize_boundary()


  raw_input()
