pipeline {
    agent any

    triggers {
        cron('H 9 * * *')
    }

    stages {
        stage('Example') {
            steps {
                echo 'Example step'
            }
        }
    }
}
stage('Archive Logs') {
    steps {
        archiveArtifacts artifacts: 'data/campaign_log.txt', fingerprint: true
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

stage('Archive Results') {
    steps {
        archiveArtifacts artifacts: 'data/*.csv', fingerprint: true
    }
}
