pipeline {
    agent any

    stages {

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Generate Offers') {
            steps {
                sh '''
                . venv/bin/activate
                python scripts/generate_offers.py
                '''
            }
        }

        stage('Send Campaign') {
            steps {
                sh '''
                . venv/bin/activate
                python scripts/send_campaign.py
                '''
            }
        }

        stage('Track Results') {
            steps {
                sh '''
                . venv/bin/activate
                python scripts/track_results.py
                '''
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'data/*.csv', fingerprint: true
            }
        }

    }
}
