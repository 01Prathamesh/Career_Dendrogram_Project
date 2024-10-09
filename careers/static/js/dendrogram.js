document.addEventListener('DOMContentLoaded', function() {
    const width = 960;
    const height = 600;

    // Updated data structure with all specified career options
    const treeData = {
        name: "Class 10th",
        children: [
            {
                name: "12th Science",
                children: [
                    { name: "Engineer" },
                    { name: "Data Analyst" },
                    { name: "Research Scientist" },
                    { name: "Healthcare Professional" },
                    { name: "Environmental Scientist" }
                ]
            },
            {
                name: "12th Commerce",
                children: [
                    { name: "Chartered Accountant" },
                    { name: "Financial Analyst" },
                    { name: "Manager" },
                    { name: "Remote Worker" },
                    { name: "Public Relations Specialist" }
                ]
            },
            {
                name: "12th Arts",
                children: [
                    { name: "Author" },
                    { name: "Graphic Designer" },
                    { name: "Content Creator" },
                    { name: "Art Teacher" },
                    { name: "Artist" },
                    { name: "Public Speaker" },
                    { name: "Child Psychologist" }
                ]
            },
            {
                name: "Vocational Courses",
                children: [
                    { name: "Mechanic" },
                    { name: "Sports Coach" },
                    { name: "Workshop Instructor" },
                    { name: "Freelancer" },
                    { name: "Startup Founder" },
                    { name: "Creative Director" },
                    { name: "Corporate Employee" },
                    { name: "Conservationist" },
                    { name: "Cybersecurity Analyst" }
                ]
            }
        ]
    };

    const svg = d3.select("#dendrogram")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(40,0)");

    const tree = d3.tree()
        .size([height, width - 160]);

    const root = d3.hierarchy(treeData);

    tree(root);

    // Create links
    svg.selectAll(".link")
        .data(root.descendants().slice(1))
        .enter().append("path")
        .attr("class", "link")
        .attr("d", d => `
            M${d.y},${d.x}
            C${d.parent.y + 100},${d.x}
             ${d.parent.y + 100},${d.parent.x}
             ${d.parent.y},${d.parent.x}
        `)
        .style("fill", "none")
        .style("stroke", "#ccc")
        .style("stroke-width", "2px");

    // Create nodes
    const node = svg.selectAll(".node")
        .data(root.descendants())
        .enter().append("g")
        .attr("class", "node")
        .attr("transform", d => `translate(${d.y},${d.x})`);

    node.append("circle")
        .attr("r", 8)
        .style("fill", "#fff")
        .style("stroke", "#333")
        .style("stroke-width", "2px");

    node.append("text")
        .attr("dy", 3)
        .attr("x", d => d.children ? -10 : 10)
        .style("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.name)
        .style("font-size", "12px")
        .style("fill", "#333");

    // Add interactivity
    node.select("circle")
        .on("mouseover", function(event) {
            d3.select(this)
                .style("fill", "#ffcc00");
        })
        .on("mouseout", function(event) {
            d3.select(this)
                .style("fill", "#fff");
        });
});
