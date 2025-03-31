// -----------------------------------------------------------------------------
// 3D-Model (OpenSCAD) for a spacer (put on the same side as the buttons)
//
// Author: Bernhard Bablok
// License: GPL3
//
// https://github.com/pcb-buttonbar
//
// -----------------------------------------------------------------------------

include <BOSL2/std.scad>
include <dimensions.scad>

//module thread_pocket(chamfer=false) {
//  p_xy = 8;            // dimensions of outer cube
//  p_z = 6.5;
//  c_d = 4;            // diameter pocket
//  c_z = 5.7;          // height pocket
//
//  if (chamfer) {
//    ch_z = 2*p_xy;
//    translate([0,0,-p_z]) rotate([180,0,90]) prism(p_xy,p_xy,ch_z,plane="yz");
//  }
//
//  translate([0,0,-p_z]) difference() {
//    cube([p_xy,p_xy,p_z]);
//    translate([(p_xy-c_d)/2,(p_xy-c_d)/2,p_z-c_z+fuzz]) cyl_00(d=c_d,h=c_z+fuzz,plane="xy");
//  }
//}

module spacer() {
  rect_tube(size=[x_spacer,y_spacer],wall=w_spacer,h=h_spacer,
	    anchor=BOTTOM+CENTER);
}

spacer();
