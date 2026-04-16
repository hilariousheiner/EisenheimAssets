// An annulus.
// License: MIT
// Copyright (c) 2026 Heiner Schmidt

module annulus(R, r, w)
{
    difference()
    {    
        linear_extrude(height = w)
        circle(r = R);
        
        translate([0,0,-0.5])
        {
            linear_extrude(height = w+1)
            circle(r = r);
        }
    }
}
annulus(1, 0.75, .1, $fn = 50);