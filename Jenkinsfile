pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-credentials')
        AWS_SECRET_ACCESS_KEY = credentials('aws-credentials')
    }

    stages {
        stage('Run Local Code') {
            steps {
                script {
                    // Ensure you have Python and necessary libraries installed
                    bat 'python -m pip install boto3'
                    bat 'set AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID% && set AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% && python athena_s3_v2.py'
                }
            }
        }
    }
}