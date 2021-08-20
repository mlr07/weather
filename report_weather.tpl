<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather</title>
</head>
<body>
    % for d in data:
        % name = d["name"]
        % sky = d["weather"][0]["main"]
        % temp = d["main"]["temp"]
	    % humid = d["main"]["humidity"]
	    % press = d["main"]["pressure"]
	    <h3>{{name}}</h3>
        <ul>
            <li>Sky: {{sky}}</li>
            <li>Temp: {{temp}}&deg;F</li>
            <li>Humidity: {{humid}}%</li>
            <li>Pressure: {{press}}hPa</li>
        </ul>
        <hr>
    % end
</body>


