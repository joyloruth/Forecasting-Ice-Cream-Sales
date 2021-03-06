{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Data Cleaning Ice Cream Data",
      "provenance": [],
      "toc_visible": true,
      "mount_file_id": "1FZpfE5dBkYB_JAem4ZNaTheRiYZl7WYc",
      "authorship_tag": "ABX9TyM9mhLHRVnYr6lh/xyLSCx7",
      "include_colab_link": true
    }, 
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/joyloruth/Forecasting-Ice-Cream-Sales/blob/master/Data_Cleaning_Ice_Cream_Data.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "763fcOUJZVjs",
        "colab_type": "text"
      },
      "source": [
        "# **Data Cleaning**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DLuoIUhccfUB",
        "colab_type": "text"
      },
      "source": [
        "### **Import Python Libraries**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0-Kl96AwagNi",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 131
        },
        "outputId": "38cb0a10-2cd4-4ab8-d681-abf81cafc516"
      },
      "source": [
        "pip install matplotlib"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.6/dist-packages (3.2.2)\n",
            "Requirement already satisfied: numpy>=1.11 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (1.18.5)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (2.8.1)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (0.10.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (1.2.0)\n",
            "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /usr/local/lib/python3.6/dist-packages (from matplotlib) (2.4.7)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.6/dist-packages (from python-dateutil>=2.1->matplotlib) (1.15.0)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nhNV_WmOaO-2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "from matplotlib import pyplot as plt\n",
        "import seaborn as sns\n",
        "%matplotlib inline"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1rkhsa7YrAlk",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from mpl_toolkits.mplot3d import Axes3D\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "import numpy as np\n",
        "import os"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FztmH-MUZk7S",
        "colab_type": "text"
      },
      "source": [
        "## **Load Revised Data**\n",
        "\n",
        "1.   Data has been pre-cleaned before this second round\n",
        "2.   In Excel I converted Celsius column into a Fahrenheit column\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jjQM8nKZXDQI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream =  pd.read_csv(\"/content/Ice Cream Data Revised.csv\", encoding=\"utf-8\")"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kqw53tncY5mB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "021609d1-b1cd-415c-c6a5-b8e0769d0d62"
      },
      "source": [
        "icecream.columns"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Celsius', 'Revenue', ' Fahrenheit', 'Unnamed: 3'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aVhn8zAyaCkM",
        "colab_type": "text"
      },
      "source": [
        "## **Preview Data, before preprocessing**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OKAiYPM_ZDy9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 191
        },
        "outputId": "5c04495a-49c7-44fd-baee-608d33956a34"
      },
      "source": [
        "icecream.head()"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Celsius</th>\n",
              "      <th>Revenue</th>\n",
              "      <th>Fahrenheit</th>\n",
              "      <th>Unnamed: 3</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>24.56688442</td>\n",
              "      <td>534.7990284</td>\n",
              "      <td>76.22039196</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>26.00519115</td>\n",
              "      <td>625.1901215</td>\n",
              "      <td>78.80934407</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>27.79055388</td>\n",
              "      <td>660.6322888</td>\n",
              "      <td>82.02299698</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>20.59533505</td>\n",
              "      <td>487.7069603</td>\n",
              "      <td>69.07160309</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>11.50349764</td>\n",
              "      <td>316.2401944</td>\n",
              "      <td>52.70629575</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       Celsius      Revenue   Fahrenheit Unnamed: 3\n",
              "0  24.56688442  534.7990284  76.22039196        NaN\n",
              "1  26.00519115  625.1901215  78.80934407        NaN\n",
              "2  27.79055388  660.6322888  82.02299698        NaN\n",
              "3  20.59533505  487.7069603  69.07160309        NaN\n",
              "4  11.50349764  316.2401944  52.70629575        NaN"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ms2OXHswb96y",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 245
        },
        "outputId": "a6e0db3f-1c66-4425-9390-d8d2c29fedb4"
      },
      "source": [
        "icecream2.isnull"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<bound method DataFrame.isnull of          Celsius      Revenue   Fahrenheit Unnamed: 3\n",
              "0    24.56688442  534.7990284  76.22039196        NaN\n",
              "1    26.00519115  625.1901215  78.80934407        NaN\n",
              "2    27.79055388  660.6322888  82.02299698        NaN\n",
              "3    20.59533505  487.7069603  69.07160309        NaN\n",
              "4    11.50349764  316.2401944  52.70629575        NaN\n",
              "..           ...          ...          ...        ...\n",
              "525          535           76          136      70-79\n",
              "526          488           69          109      60-69\n",
              "527          316           53           65      50-59\n",
              "528          238           48           31      40-49\n",
              "529           55           34            5      30-39\n",
              "\n",
              "[530 rows x 4 columns]>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ll2h7mOLaUmm",
        "colab_type": "text"
      },
      "source": [
        "### **Drop Columns**\n",
        "\n",
        "**Remove Redundancies**\n",
        "\n",
        "*   Remove Column \"Unnamed: 3\" , there are no values in this column\n",
        "\n",
        "**Remove Null Values**\n",
        "\n",
        "*   Remove Celsisus column, as it provides the same infromation in the Farhenhiet but in a different metric\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TZcpxj_-YLeN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream = icecream.drop(['Unnamed: 3'], axis = 1)"
      ],
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "G9EyDE_lYmfx",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream = icecream.drop(['Celsius'], axis= 1)"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N9yrAxGkc97X",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 33
        },
        "outputId": "6560c114-a323-406a-8f71-62557534485a"
      },
      "source": [
        "icecream.columns"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Revenue', ' Fahrenheit'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9F5eg9XMlphF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 163
        },
        "outputId": "ce2b29b4-bdd9-4940-cab1-7471fcbe7538"
      },
      "source": [
        "icecream.info()"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 530 entries, 0 to 529\n",
            "Data columns (total 2 columns):\n",
            " #   Column       Non-Null Count  Dtype \n",
            "---  ------       --------------  ----- \n",
            " 0   Revenue      510 non-null    object\n",
            " 1    Fahrenheit  510 non-null    object\n",
            "dtypes: object(2)\n",
            "memory usage: 8.4+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8y2TVScrrd98",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream = icecream.drop(['Celsius'], axis =1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yOotofFdlYrG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "outputId": "eb0b3a8b-daf7-4b1c-a676-23b3619e2b48"
      },
      "source": [
        "icecream"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Revenue</th>\n",
              "      <th>Fahrenheit</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>534.7990284</td>\n",
              "      <td>76.22039196</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>625.1901215</td>\n",
              "      <td>78.80934407</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>660.6322888</td>\n",
              "      <td>82.02299698</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>487.7069603</td>\n",
              "      <td>69.07160309</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>316.2401944</td>\n",
              "      <td>52.70629575</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>525</th>\n",
              "      <td>76</td>\n",
              "      <td>136</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>526</th>\n",
              "      <td>69</td>\n",
              "      <td>109</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>527</th>\n",
              "      <td>53</td>\n",
              "      <td>65</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>528</th>\n",
              "      <td>48</td>\n",
              "      <td>31</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>529</th>\n",
              "      <td>34</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>530 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "         Revenue   Fahrenheit\n",
              "0    534.7990284  76.22039196\n",
              "1    625.1901215  78.80934407\n",
              "2    660.6322888  82.02299698\n",
              "3    487.7069603  69.07160309\n",
              "4    316.2401944  52.70629575\n",
              "..           ...          ...\n",
              "525           76          136\n",
              "526           69          109\n",
              "527           53           65\n",
              "528           48           31\n",
              "529           34            5\n",
              "\n",
              "[530 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xDaosEiZdcyf",
        "colab_type": "text"
      },
      "source": [
        "## **Rename Column**\n",
        "\n",
        "*   Change column name \"Fahrenheit\" to \"Temperature\"\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZpIcW4Z-mMiO",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "8fa62358-0384-47ea-9862-5d5d7eda12cb"
      },
      "source": [
        "icecream.columns.values"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array(['Revenue', ' Fahrenheit'], dtype=object)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8zzr43uIm3RI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "column_names = ['Revenue','Temperature']"
      ],
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t2vVi0euozro",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream.columns = column_names"
      ],
      "execution_count": 32,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LbTl0KZadhop",
        "colab_type": "text"
      },
      "source": [
        "## **Reorder Columns**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h5gxfksjrPB3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "reorder_columns = ['Temperature', 'Revenue']"
      ],
      "execution_count": 33,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HA7hz6nXo9sH",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "outputId": "1aee65df-6380-49d9-c947-d09b4cbcaa21"
      },
      "source": [
        "icecream[reorder_columns]"
      ],
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Temperature</th>\n",
              "      <th>Revenue</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>76.22039196</td>\n",
              "      <td>534.7990284</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>78.80934407</td>\n",
              "      <td>625.1901215</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>82.02299698</td>\n",
              "      <td>660.6322888</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>69.07160309</td>\n",
              "      <td>487.7069603</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>52.70629575</td>\n",
              "      <td>316.2401944</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>525</th>\n",
              "      <td>136</td>\n",
              "      <td>76</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>526</th>\n",
              "      <td>109</td>\n",
              "      <td>69</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>527</th>\n",
              "      <td>65</td>\n",
              "      <td>53</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>528</th>\n",
              "      <td>31</td>\n",
              "      <td>48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>529</th>\n",
              "      <td>5</td>\n",
              "      <td>34</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>530 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Temperature      Revenue\n",
              "0    76.22039196  534.7990284\n",
              "1    78.80934407  625.1901215\n",
              "2    82.02299698  660.6322888\n",
              "3    69.07160309  487.7069603\n",
              "4    52.70629575  316.2401944\n",
              "..           ...          ...\n",
              "525          136           76\n",
              "526          109           69\n",
              "527           65           53\n",
              "528           31           48\n",
              "529            5           34\n",
              "\n",
              "[530 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Hqn7X0AYjXEC",
        "colab_type": "text"
      },
      "source": [
        "## **Export Cleaned Data into a CSV File**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-01jzCH7izoX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream.to_csv('/content/icecreamdcleaned.csv')"
      ],
      "execution_count": 35,
      "outputs": []
    }
  ]
}
