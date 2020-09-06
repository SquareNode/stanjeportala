const models = require('../models/models');

module.exports.home = async function(req,res,next) {
	
	try {
		
		let files, date;
		if(req.query.hasOwnProperty('date')) {
			files = await models.getData(req.query['date']);
			date = req.query['date'];
		}
		else {
			files = await models.getData();
			const d = new Date();
			date = d.getDate() + "." +  (d.getMonth() + 1) + "." + d.getFullYear();
		}
		
		res.render('home', {
			data: files,
			req_date: date
		});
	}catch(err) {
		console.log(err);
	}
	
};

