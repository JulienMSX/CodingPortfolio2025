//Julien Massaux English To French

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

const int maxwords = 50;
const int wl = 30;

int read_in(char e[][wl], char f[][wl]);
void sort_words(char e[][wl], char f[][wl], int n);
void search_words(char e[][wl], char f[][wl], int n);
void write_out(char e[][wl], char f[][wl], int n);

void main() {
    char english[maxwords][wl];
    char french[maxwords][wl];
    int count = read_in(english, french);
    sort_words(english, french, count);
    write_out(english, french, count);
    search_words(english, french, count);
}

int read_in(char e[][wl], char f[][wl]) {
    ifstream infile("dict.dat");
    int count = 0;
    while (count < maxwords && infile >> e[count] >> f[count]) {
        count++;
    }

    infile.close();
    return count;
}

void sort_words(char e[][wl], char f[][wl], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min = i;
        for (int j = i + 1; j < n; j++) {
            if (strcmp(e[j], e[min]) < 0) {
                min = j;
            }
        }
        if (min != i) {
            char temp[wl];
            strcpy_s(temp, e[i]);
            strcpy_s(e[i], e[min]);
            strcpy_s(e[min], temp);
            strcpy_s(temp, f[i]);
            strcpy_s(f[i], f[min]);
            strcpy_s(f[min], temp);
        }
    }
}
void search_words(char e[][wl], char f[][wl], int n) {
    char w[wl];
    cout << "Enter word to translate: ";
    cin >> w;
    while (true) {
        bool find = false;
        for (int i = 0; i < n; i++) {
            if (strcmp(e[i], w) == 0) {
                cout << f[i] << endl;
                find = true;
                break;
            }
        }
        cin >> w;
    }
}
void write_out(char e[][wl], char f[][wl], int n) {
    for (int i = 0; i < n; i++) {
        cout << e[i] << " " << f[i] << endl;
    }
}
