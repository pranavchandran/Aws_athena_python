pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id') // Ensure 'aws-access-key-id' is the correct ID in Jenkins credentials
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key') // Ensure 'aws-secret-access-key' is the correct ID in Jenkins credentials
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install boto3'
                }
            }
        }
        stage('Run Athena Query') {
            steps {
                script {
                    bat '''
                    set AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID%
                    set AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY%
                    python athena_s3_v2.py
                    '''
                }
            }
        }
    }
}
