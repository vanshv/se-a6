pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vanshv/se-a6.git'
            }
        }
        stage('Send confirmation'){
            steps{
                echo 'repo cloned successfully!\ntesting started...'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x main.py"
                sh "./main.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
