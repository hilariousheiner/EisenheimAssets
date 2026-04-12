// License: CC BY-NC-ND 4.0 (https://creativecommons.org/licenses/by-nc-nd/4.0/)
// Author: Heiner
// Commercial use requires a separate license

//engine();
//bridge(); 
//hull();
//wingL();
//wingR();
ship();

module ship()
{
    union()
    {
        translate([-4, 0, 0])
        {
            bridge();
        }
        translate([-2, 0, 0])
        {
            union()
            {
                wingL();
                hull();
                wingR();
            }
        }
        engine();
    }
}

module bridge()
{
    scale([1.5, 1, 1])
    {
        difference()
        {
            sphere(r = 1.25, $fn = 50);
            translate([1.5,0,0])
            {
                cube(size = 3, center = true);
            }
        }
    }
}

module wingL()
{
    difference()
    {   
        translate([-.25, 0, 0])
        {
            rotate([90, 0, 10])
            {
                wing();
            }
        }
        hull();
    }
}
module wingR()
{
    difference()
    {
        translate([-0.25, 0, 0])
        {
            rotate([-90, 0, -10])
            {
                wing();
            }
        }
        hull(); 
    }
}

module wing()
{
    linear_extrude(height = 5, scale = 0.75)
    {
        scale([.75, 0.125, 1])
        {
            circle(r = 1.5, $fn = 50);
        }
    }
}
 
module hull()
{
    rotate([0,90,0])
    {       
        linear_extrude(center = true, height = 4)     
        circle(r = 1.5, $fn = 50);
    }
}

module engine() 
{
    rotate([0,90,0])
    {
        difference()
        {
            {
                linear_extrude(height = 2, scale = 2)    
                circle(r = 1, $fn = 50);
            }
            {
                linear_extrude(height = 3, scale = 2)    
                circle(r = 1, $fn = 50);
            }
        }
    }
}