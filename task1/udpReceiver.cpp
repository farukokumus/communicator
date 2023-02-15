#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <zlib.h>
#include <chrono>

const int BUF_SIZE = 1024;
const int PORT = 25042;
const char* IP_ADDR = "127.0.0.1";

bool check_checksum(double* rot, uint32_t received_checksum) {
    // Compute the expected checksum
    ulong expected_checksum = crc32(0L, Z_NULL, 0);
    expected_checksum = crc32(expected_checksum, reinterpret_cast<Bytef*>(rot), sizeof(double)*9);
    //expected_checksum = ~expected_checksum & 0xffffffff;
    std::cout << "Checksum: " <<expected_checksum << "\t";
    // Compare the expected checksum to the received checksum
    return received_checksum == expected_checksum;
}

void extract_data(char* buffer, double* rotation_matrix,uint32_t& check) {
    memcpy(rotation_matrix, buffer, sizeof(double) * 9);
    memcpy(&check, buffer + sizeof(double) * 9, sizeof(uint32_t));
    
}

void printMatrix(double matrix[9]) {
    for (int i = 0; i < 9; i++) {
        std::cout << matrix[i] << ", ";
        if ( (i+1) % 3 == 0)
            std::cout << std::endl;
    }
}

int main() {
    int sockfd;
    socklen_t len;
    char buffer[BUF_SIZE];
    struct sockaddr_in servaddr, cliaddr;

    // Create socket
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    // Clear servaddr and set fields
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr(IP_ADDR);
    servaddr.sin_port = htons(PORT);

    // Bind socket to address
    bind(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr));
    int message_count = 0;
    auto start_time = std::chrono::high_resolution_clock::now();
    while (true) {
        len = sizeof(cliaddr);
        // Receive message
        int n = recvfrom(sockfd, buffer, BUF_SIZE, 0, (struct sockaddr *) &cliaddr, &len);



        // Extract rotation matrix message
        double rotation_matrix[9];
        uint32_t check;
        extract_data(buffer, rotation_matrix,check);

        // Print rotation matrix
        printMatrix(rotation_matrix);


        message_count++;
        auto current_time = std::chrono::high_resolution_clock::now();
        auto elapsed_time = current_time - start_time;
        //if (elapsed_time >= std::chrono::seconds(1)) {
            double rate = message_count / std::chrono::duration<double>(elapsed_time).count();
            std::cout << "Incoming message rate: " << rate << " Hz" << std::endl;

            // Reset the message count and start time for the next measurement
            message_count = 0;
            start_time = current_time;
        //}

        // Check CRC
        bool crc_check = check_checksum(rotation_matrix, check);
        if (crc_check) {
            std::cout << "Checksum is correct." << std::endl;
        } else {
            std::cout << "Checksum is incorrect." << std::endl;

        }
    }

    close(sockfd);
    return 0;
}



