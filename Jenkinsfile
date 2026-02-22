pipeline {
    agent any
    
    environment {
        MY_API_KEY = credentials('weather-api-key')
        IMAGE_NAME = "flask-monitor-app"
    }

    stages {
        stage('1. Pobieranie') {
            steps {
                deleteDir()
                sh 'git clone https://github.com/dominik-mzg/jenkins1.git .'
            }
        }

        stage('2. Build i Deploy') {
            steps {
                script {
                    sh "docker stop ${IMAGE_NAME} || true"
                    sh "docker rm ${IMAGE_NAME} || true"
                    sh "docker build -t ${IMAGE_NAME} ."
                    sh "docker run -d --network moja-siec --name ${IMAGE_NAME} -p 5000:5000 -e MY_API_KEY=${MY_API_KEY} ${IMAGE_NAME}"
                }
            }
        }

        stage('3. Test') {
            steps {
                sleep 5
                sh "curl http://${IMAGE_NAME}:5000"
            }
        }
    }
}
