document.addEventListener('DOMContentLoaded', function() {
    const width = 960;
    const height = 600;

    // Updated data structure with all links pointing to Wikipedia
    const treeData = {
        name: "Class 10th",
        children: [
            {
                name: "12th Science",
                url: "science",
                children: [
                    { name: "Engineer", url: "engineering" },
                    { name: "Data Analyst", url: "data_analyst" },
                    { name: "Research Scientist", url: "research_scientist" },
                    { name: "Healthcare Professional", url: "healthcare_professional" },
                    { name: "Environmental Scientist", url: "environmental_scientist" }
                ]
            },
            {
                name: "12th Commerce",
                url: "commerce",
                children: [
                    { name: "Chartered Accountant", url: "ca" },
                    { name: "Financial Analyst", url: "financial_analyst" },
                    { name: "Manager", url: "manager" },
                    { name: "Remote Worker", url: "remote_worker" },
                    { name: "Public Relations Specialist", url: "PR_specialist" }
                ]
            },
            {
                name: "12th Arts",
                url: "arts",
                children: [
                    { name: "Author", url: "author" },
                    { name: "Graphic Designer", url: "graphic_designer" },
                    { name: "Content Creator", url: "content_creator" },
                    { name: "Art Teacher", url: "art_teacher" },
                    { name: "Artist", url: "artist" },
                    { name: "Public Speaker", url: "public_speaker" },
                    { name: "Child Psychologist", url: "child_psychologist" }
                ]
            },
            {
                name: "Vocational Courses",
                url: "vocational_courses",
                children: [
                    { name: "Mechanic", url: "mechanic" },
                    { name: "Sports Coach", url: "sport_coach" },
                    { name: "Workshop Instructor", url: "work_instructor" },
                    { name: "Freelancer", url: "freelancer" },
                    { name: "Startup Founder", url: "startup_founder" },
                    { name: "Creative Director", url: "creative_director" },
                    { name: "Corporate Employee", url: "corporate_employee" },
                    { name: "Conservationist", url: "conservation" },
                    { name: "Cybersecurity Analyst", url: "cybersecurity_analyst" }
                ]
            }
        ]
    };

    const svg = d3.select("#dendrogram")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(90,0)");

    const tree = d3.tree()
        .size([height, width - 300]);

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
        .style("stroke-width", "2px")
        .on("click", (event, d) => {
            const url = d.data.url;
            if (url) {
                window.open(url, '_blank'); // Opens the URL in a new tab
            }
        });

    node.append("text")
        .attr("dy", 3)
        .attr("x", d => d.children ? -10 : 10)
        .style("text-anchor", d => d.children ? "end" : "start")
        .text(d => d.data.name)
        .style("font-size", "16px")
        .style("fill", "#333");

    // Add interactivity for hover
    node.select("circle")
        .on("mouseover", function() {
            d3.select(this).style("fill", "#ffcc00");
        })
        .on("mouseout", function() {
            d3.select(this).style("fill", "#fff");
        });
});
