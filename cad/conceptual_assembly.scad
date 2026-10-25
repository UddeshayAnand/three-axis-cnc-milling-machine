// Millimetres
$fn = 32;
base_width = 615;
base_depth = 425;
upright_height = 390;
board = 17;
base_rail = 25;
rail_d = 8;
table_offset = 0;
carriage_offset = 0;

module beam(size, position) {
    color([0.66, 0.46, 0.26]) translate(position) cube(size);
}
module rod(length, position, rotation) {
    color("silver") translate(position) rotate(rotation) cylinder(h=length, d=rail_d);
}
module motor(position) {
    // Illustrative 57 mm envelope; not a verified part model.
    color([0.18,0.19,0.21]) translate(position) cube([57,57,65]);
}
module base() {
    beam([base_width,base_rail,board],[0,0,0]);
    beam([base_width,base_rail,board],[0,base_depth-base_rail,0]);
    beam([base_rail,base_depth,board],[0,0,0]);
    beam([base_rail,base_depth,board],[base_width-base_rail,0,0]);
}
module gantry() {
    beam([base_rail,board,upright_height],[0,base_depth-55,board]);
    beam([base_rail,board,upright_height],[base_width-base_rail,base_depth-55,board]);
    beam([base_width,board,base_rail],[0,base_depth-55,upright_height]);
    rod(base_width-50,[25,base_depth-70,170],[0,90,0]);
    rod(base_width-50,[25,base_depth-70,320],[0,90,0]);
    rod(base_width-50,[25,base_depth-70,245],[0,90,0]); // screw represented as rod
    motor([base_width-65,base_depth-95,210]);
}
module table() {
    rod(base_depth-50,[180,25,48],[-90,0,0]);
    rod(base_depth-50,[435,25,48],[-90,0,0]);
    rod(base_depth-50,[307.5,25,40],[-90,0,0]);
    beam([320,230,17],[147.5,70+table_offset,60]);
    motor([279,0,18]);
}
module carriage() {
    translate([carriage_offset,0,0]) {
        beam([150,17,190],[232.5,base_depth-100,145]);
        rod(150,[255,base_depth-120,165],[0,0,0]);
        rod(150,[360,base_depth-120,165],[0,0,0]);
        rod(150,[307.5,base_depth-120,165],[0,0,0]);
        beam([150,95,17],[232.5,base_depth-190,180]);
        motor([279,base_depth-145,335]);
        color("teal") translate([307.5,base_depth-155,165]) cylinder(h=90,d=45);
    }
}
base();
gantry();
table();
carriage();
