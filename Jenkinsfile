pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('aws_secret_access_key')
    }

    stages {
        stage('Run Local Code') {
            steps {
                script {
                    // Ensure you have Python and necessary libraries installed
                    sh 'python3 -m pip install boto3'
                    sh 'python3 athena_s3_v2.py'
                }
            }
        }
    }
}