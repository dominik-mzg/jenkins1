pipeline{
	agent any
	environment{
		MY_API_KEY = credentials('weather-api-key')
		IMAGE_NAME = "weather-app-practice"
	}
	stages{
		stage('1. Setup'){
			steps{
				deleteDir()
				sh 'git clone https://github.com/dominik-mzg/jenkins1.git .'
			}
		}

		stage('2. Budowanie i Deploy') {
            	  steps {
                    script {
                      sh "docker stop ${IMAGE_NAME} || true"
                      sh "docker rm ${IMAGE_NAME} || true"
                      sh "docker build -t ${IMAGE_NAME}:latest ."
                    
                    // DODAJEMY: --network moja-siec
                    sh "docker run -d --network moja-siec --name ${IMAGE_NAME} -p 3000:3000 -e MY_API_KEY=${MY_API_KEY} ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('3. Test Działania') {
            steps {
                sleep 5
                // TERAZ: łączymy się bezpośrednio po nazwie kontenera!
                // Jenkins musi być w tej samej sieci, żeby to zadziałało
                sh "curl http://${IMAGE_NAME}:3000"
            }
        }
