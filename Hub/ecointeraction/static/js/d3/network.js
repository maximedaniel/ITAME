var w = document.getElementById('div-network').offsetWidth,
    h = document.getElementById('div-network').offsetHeight;
	
var zoom = d3.behavior.zoom()
    .scaleExtent([-10, 10])
    .on("zoom", zoomed);
	
var labelDistance = 0;

var vis = d3.select("#div-network").append("svg:svg").attr("width", w).attr("height", h).call(zoom);

function zoomed() {
  vis.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}

var nodes = [];
var labelAnchors = [];
var labelAnchorLinks = [];
var links = [];
d3.json("data/data.json", function(error, graph) {
  if (error) throw error;
  
for(var i = 0; i < graph.nodes.length; i++) {
	var node = graph.nodes[i];
	nodes.push(node);
	labelAnchors.push({
		node : node
	});
	labelAnchors.push({
		node : node
	});
	labelAnchorLinks.push({
		source : i * 2,
		target : i * 2 + 1,
		weight : 1
	});
};

for(var i = 0; i < graph.links.length; i++) {
	var link = graph.links[i];
	links.push(link);
};
var force = d3.layout.force().size([w, h]).nodes(nodes).links(links).gravity(1).linkDistance(function(d) { return d.length*10;}).charge(-3000).linkStrength(function(x) {
	return x.weight * 10
});


force.start();

var force2 = d3.layout.force().nodes(labelAnchors).links(labelAnchorLinks).gravity(0).linkDistance(0).linkStrength(8).charge(-100).size([w, h]);
force2.start();

var link = vis.selectAll("line.link").data(links).enter().append("svg:line").attr("class", "link");

var node = vis.selectAll("g.node").data(force.nodes()).enter().append("svg:g").attr("class", "node");
node.append("svg:circle").attr("r", function(d) { return d.size; }).style("fill", function(d) { return "hsla("+d.group+")"; }).style("stroke", "#000");
node.call(force.drag);


var anchorLink = vis.selectAll("line.anchorLink").data(labelAnchorLinks)//.enter().append("svg:line").attr("class", "anchorLink").style("stroke", "#999");

var anchorNode = vis.selectAll("g.anchorNode").data(force2.nodes()).enter().append("svg:g").attr("class", "anchorNode");
anchorNode.append("svg:circle").attr("r", 0).style("fill", "#000");
	anchorNode.append("svg:text").text(function(d, i) {
	return i % 2 == 0 ? "" : d.node.name
});

var updateLink = function() {
	this.attr("x1", function(d) {
		return d.source.x;
	}).attr("y1", function(d) {
		return d.source.y;
	}).attr("x2", function(d) {
		return d.target.x;
	}).attr("y2", function(d) {
		return d.target.y;
	});

}

var updateNode = function() {
	this.attr("transform", function(d) {
		return "translate(" + d.x + "," + d.y + ")";
	});

}


force.on("tick", function() {

	force2.start();

	node.call(updateNode);

	anchorNode.each(function(d, i) {
		if(i % 2 == 0) {
			d.x = d.node.x;
			d.y = d.node.y;
		} else {
			var b = this.childNodes[1].getBBox();

			var diffX = d.x - d.node.x;
			var diffY = d.y - d.node.y;

			var dist = Math.sqrt(diffX * diffX + diffY * diffY);

			var shiftX = b.width * (diffX - dist) / (dist * 2);
			shiftX = Math.max(-b.width, Math.min(0, shiftX));
			var shiftY = 5;
			this.childNodes[1].setAttribute("transform", "translate(" + shiftX + "," + shiftY + ")");
		}
	});


	anchorNode.call(updateNode);

	link.call(updateLink);
	anchorLink.call(updateLink);

});
});