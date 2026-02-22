pipeline {
    agent any // Uruchom na dowolnym dostępnym agencie

    stages {
        stage('Przygotowanie') {
            steps {
                echo 'Pobieranie zależności...'
                // Używamy obrazu node, żeby nie instalować go na systemie
                sh 'npm install'
            }
        }

        stage('Testy Jednostkowe') {
            steps {
                echo 'Uruchamiam testy...'
                sh 'npm test'
            }
        }

        stage('Budowanie (Build)') {
            steps {
                echo 'Pakowanie aplikacji...'
                sh 'tar -czf app.tar.gz app.js package.json'
            }
        }
    }

    post {
        always {
            echo 'Koniec pracy. Czyszczenie środowiska.'
        }
        success {
            echo 'SUKCES: Aplikacja przetestowana i gotowa! Mozesz ją uruchomić'
        }
        failure {
            echo 'BŁĄD: Testy nie przeszły, sprawdź logi!'
        }
    }
}
