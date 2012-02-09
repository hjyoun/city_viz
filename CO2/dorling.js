// Ratio of Obese (BMI >= 30) in U.S. Adults, CDC 2008
var datamsa = [];
d3.json("vulcan_total_msa.json", function(json) { datamsa = json; });

var color = d3.scale.linear()
    .domain([500, 4000])
    .range(["#3182bd", "#e6550d"]); 

var force = d3.layout.force()
    .charge(0)
    .gravity(0)
    .size([960, 500]);

//var svg = d3.select("#chart").append("svg:svg")
    //.attr("width", 960 + 100)
    //.attr("height", 500 + 100)
  //.append("svg:g")
    //.attr("transform", "translate(50,50)");

//{"type":"FeatureCollection", "features":[
//{"type":"Feature","id":"1","geometry":{"type":"Point","coordinates":[-103.228,44.076]},"properties":{"name":"Rapid City, SD","population": 115285.0}},

d3.json("../usa_geo/us-msa-centroids.json", function(mm) {
  var project = d3.geo.albersUsa(),
      idToNode = {},
      links = [],
      nodes = mm.features.map(function(d) {
    var xy = project(d.geometry.coordinates);
    return idToNode[d.id] = {
      x: xy[0],
      y: xy[1],
      gravity: {x: xy[0], y: xy[1]},
      r: Math.sqrt(datamsa[d.id] * 0.00002),
      value: datamsa[d.id],
			name: d.properties.name
    };
  });

  force
      .nodes(nodes)
      .links(links)
      .start()
      .on("tick", function(e) {
    var k = e.alpha,
        kg = k * .02;
    nodes.forEach(function(a, i) {
      // Apply gravity forces.
      a.x += (a.gravity.x - a.x) * kg;
      a.y += (a.gravity.y - a.y) * kg;
      nodes.slice(i + 1).forEach(function(b) {
        // Check for collisions.
        var dx = a.x - b.x,
            dy = a.y - b.y,
            l = Math.sqrt(dx * dx + dy * dy),
            d = a.r + b.r;
        if (l < d) {
          l = (l - d) / l * k;
          dx *= l;
          dy *= l;
          a.x -= dx;
          a.y -= dy;
          b.x += dx;
          b.y += dy;
        }
      });
    });

    msa.selectAll("circle")
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("stroke","black");
  });

  msa.selectAll("circle")
      .data(nodes)
    .enter().append("svg:circle")
      .style("fill", function(d) { return color(Math.sqrt(d.value)); })
      .attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; })
      .attr("r", function(d, i) { return d.r; })
      .attr("title", function(d, i) { return d.name+' : '+d.value; });
      //.on("mouseover", mouseover );

	$("#msas circle[title]").tooltip();
		//function mouseover(d, i) {
				//infotext1.text("City:  "+d.name);
				//infotext2.text("Total Emission: "+d.value);
		//}

});
