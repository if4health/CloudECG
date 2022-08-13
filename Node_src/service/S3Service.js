require('dotenv').config();
const S3 = require('aws-sdk/clients/s3');

const bucketName = process.env.AWS_BUCKET_NAME;
const region = process.env.AWS_BUCKET_REGION;
const accessKeyId = process.env.AWS_ACCESS_KEY;
const secretAccessKey = process.env.AWS_SECRET_KEY;


const s3 = new S3({
    region,
    accessKeyId,
    secretAccessKey
})

class S3Service {

    async upload(fileName, data) {
        var params = {
            Bucket: bucketName,
            Key: fileName,
            Body: data,
            ContentType: "application/plan-text"
        };
        return s3.upload(params).promise()
    }

}

module.exports = new S3Service();