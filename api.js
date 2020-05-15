const Curricula = {
	URL: 'https://www.fsinf.at/files/curricula/',

	getIndex: async function(){
		let res = await fetch(this.URL + '/index.json');
		return await res.json();
	},

	getCurriculum: async function(code){
		let res = await fetch(this.URL + code + '.json');
		let curriculum = await res.json();

		function linkGroup(group, curriculum){
			curriculum.groups[group.name] = group;
			if (group.groups)
				group.groups.forEach(g => {
					linkGroup(g, curriculum);
					g.parent = group;
				});
			if (group.courses){
				group.courses = group.courses.map(c => curriculum.courses[c]);
				group.courses.forEach(c => {c.parent = group;});
			}
		}

		curriculum.groups = {};
		linkGroup(curriculum.group, curriculum);
		return curriculum;
	}
};
