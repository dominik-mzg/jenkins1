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

		stage('2. Budowanie i Deploy'){
            		steps {
                		script {
                    		// 1. Zabij stary kontener, żeby zwolnić port 3000
                    		sh "docker stop ${IMAGE_NAME} || true"
                    		sh "docker rm ${IMAGE_NAME} || true"
                    
                    		// 2. Buduj obraz
                    		sh "docker build -t ${IMAGE_NAME}:latest ."
                    
                    		// 3. Odpal nowy kontener z kluczem
                    		sh "docker run -d -p 3000:3000 --name ${IMAGE_NAME} -e MY_API_KEY=${MY_API_KEY} ${IMAGE_NAME}:latest"
			}
		}

	}
	stage('3. Test'){
		steps{
			sleep 3
			sh 'curl http://localhost:3000'
		}
	}
}
		
}

