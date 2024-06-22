pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install boto3'
                }
            }
        }
        stage('Verify Credentials') {
            steps {
                script {
                    bat '''
                    echo AWS_ACCESS_KEY_ID: %AWS_ACCESS_KEY_ID:~0,4%****
                    echo AWS_SECRET_ACCESS_KEY: %AWS_SECRET_ACCESS_KEY:~0,4%****
                    aws sts get-caller-identity
                    '''
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
