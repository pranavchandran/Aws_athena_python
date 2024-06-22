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
                    // Print environment variables
                    // Check if environment variables exist
                    if (env.AWS_ACCESS_KEY_ID == null || env.AWS_SECRET_ACCESS_KEY == null) {
                        error("AWS credentials not found")
                    }
                    // Ensure you have Python and necessary libraries installed
                    bat 'python -m pip install boto3'
                    bat 'set AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID% && set AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% && python athena_s3_v2.py'
                }
            }
        }
    }
}