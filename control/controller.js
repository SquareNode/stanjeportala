const models = require('../models/models');

module.exports.home = async function(req,res,next) {
	
	try {
		const files = await models.getData();
		
		res.render('home', {
			data: files
		});
	}catch(err) {
		console.log(err);
	}
	
};

