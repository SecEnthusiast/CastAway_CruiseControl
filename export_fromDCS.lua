-- Open the CSV file for writing
file = io.open("targets.csv", "w")

-- Write the headers to the CSV file
file:write("Target ID,Distance (m),Radar Cross Section (m^2),Angle (deg),Speed (km/h)\n")

-- Iterate through all enemy targets within 10km
for i, target in ipairs(sensor_data:getTargetsByTypeRadar("enemy", 10000)) do
    -- Get the target data
    distance = target:getDistance()
    rcs = target:getRCS()
    angle = math.deg(target:getAngle())
    speed = target:getSpeed()*3.6 -- Convert m/s to km/h

    -- Write the target data to the CSV file
    file:write(target:getID() .. "," .. distance .. "," .. rcs .. "," .. angle .. "," .. speed .. "\n")
end

-- Close the CSV file
file:close()
