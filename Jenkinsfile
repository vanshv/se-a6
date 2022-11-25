pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vanshv/se-a6.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Code.py"
                sh "./Code.py"
            }
        }
        stage('Test Code for positive') {
            steps {
                sh "chmod u+x TestPass.py"
                sh "./TestPass.py"
            }
        }
        stage('Test Code for negative') {
            steps {
                sh "chmod u+x TestFail.py"
                sh "./TestFail.py"
            }
        }
    } 
}
