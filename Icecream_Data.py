{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Icecream Data",
      "provenance": [],
      "mount_file_id": "1iUfa9izROiSY8chs7ufoe1ft7W0_QnF0",
      "authorship_tag": "ABX9TyNgpS0sNAfGc1v82oCr8Oyw",
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
        "<a href=\"https://colab.research.google.com/github/joyloruth/salesfunnel/blob/master/Icecream_Data.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DLuoIUhccfUB",
        "colab_type": "text"
      },
      "source": [
        "Import Python Libraries"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0-Kl96AwagNi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "pip install matplotlib"
      ],
      "execution_count": null,
      "outputs": []
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
      "execution_count": 64,
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
      "execution_count": 63,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XlZaTLeHZpRN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream2 = pd.read_csv(\"/icecreamdata - Sheet1.csv\", encoding=\"utf-8\")"
      ],
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nIAy9al_YPDo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream = icecream2.copy()"
      ],
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FOkDzRv1lPgm",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 198
        },
        "outputId": "7eccebbe-7304-4cee-e098-2fadbed522a8"
      },
      "source": [
        "icecream.tail()"
      ],
      "execution_count": 125,
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
              "      <th>495</th>\n",
              "      <td>524.746364</td>\n",
              "      <td>72.094819</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>755.818399</td>\n",
              "      <td>91.207566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>306.090719</td>\n",
              "      <td>54.658683</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>566.217304</td>\n",
              "      <td>72.252324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>655.660388</td>\n",
              "      <td>84.123925</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     Temperature    Revenue\n",
              "495   524.746364  72.094819\n",
              "496   755.818399  91.207566\n",
              "497   306.090719  54.658683\n",
              "498   566.217304  72.252324\n",
              "499   655.660388  84.123925"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WeZXnVBqlevn",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 288
        },
        "outputId": "f7098f2e-f27a-48ba-e0b0-fb08caac9208"
      },
      "source": [
        "icecream.describe()"
      ],
      "execution_count": 126,
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
              "      <th>count</th>\n",
              "      <td>500.000000</td>\n",
              "      <td>500.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>521.570777</td>\n",
              "      <td>72.018005</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>175.404751</td>\n",
              "      <td>14.573498</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>10.000000</td>\n",
              "      <td>32.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>405.558681</td>\n",
              "      <td>62.820064</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>529.368565</td>\n",
              "      <td>72.307023</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>642.257922</td>\n",
              "      <td>81.933214</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>1000.000000</td>\n",
              "      <td>113.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "       Temperature     Revenue\n",
              "count   500.000000  500.000000\n",
              "mean    521.570777   72.018005\n",
              "std     175.404751   14.573498\n",
              "min      10.000000   32.000000\n",
              "25%     405.558681   62.820064\n",
              "50%     529.368565   72.307023\n",
              "75%     642.257922   81.933214\n",
              "max    1000.000000  113.000000"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 126
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
          "height": 181
        },
        "outputId": "74223fb1-3444-414e-8ba4-90875784790a"
      },
      "source": [
        "icecream.info()"
      ],
      "execution_count": 123,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 500 entries, 0 to 499\n",
            "Data columns (total 2 columns):\n",
            " #   Column       Non-Null Count  Dtype  \n",
            "---  ------       --------------  -----  \n",
            " 0   Temperature  500 non-null    float64\n",
            " 1   Revenue      500 non-null    float64\n",
            "dtypes: float64(2)\n",
            "memory usage: 7.9 KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_CHXhdjomMJo",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "sns.barplot(\n",
        "  data=icecream ,\n",
        "\tx=\"Celsius\" ,\n",
        "  y=\"Revenue\"\n",
        " )\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JVCBuUzFkJxN",
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
        "id": "8y2TVScrrd98",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream = icecream.drop(['Celsius'], axis =1)"
      ],
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yOotofFdlYrG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 407
        },
        "outputId": "1883dd4c-c889-482d-91a8-d3d5315736b7"
      },
      "source": [
        "icecream"
      ],
      "execution_count": 48,
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
              "      <td>534.799028</td>\n",
              "      <td>76.220392</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>625.190122</td>\n",
              "      <td>78.809344</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>660.632289</td>\n",
              "      <td>82.022997</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>487.706960</td>\n",
              "      <td>69.071603</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>316.240194</td>\n",
              "      <td>52.706296</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>524.746364</td>\n",
              "      <td>72.094819</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>755.818399</td>\n",
              "      <td>91.207566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>306.090719</td>\n",
              "      <td>54.658683</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>566.217304</td>\n",
              "      <td>72.252324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>655.660388</td>\n",
              "      <td>84.123925</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "        Revenue   Fahrenheit\n",
              "0    534.799028    76.220392\n",
              "1    625.190122    78.809344\n",
              "2    660.632289    82.022997\n",
              "3    487.706960    69.071603\n",
              "4    316.240194    52.706296\n",
              "..          ...          ...\n",
              "495  524.746364    72.094819\n",
              "496  755.818399    91.207566\n",
              "497  306.090719    54.658683\n",
              "498  566.217304    72.252324\n",
              "499  655.660388    84.123925\n",
              "\n",
              "[500 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 48
        }
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
      "execution_count": 50,
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
        "column_names = ['Temperature','Revenue']"
      ],
      "execution_count": 52,
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
      "execution_count": 55,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "h5gxfksjrPB3",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream3.columns = column_names"
      ],
      "execution_count": 86,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HA7hz6nXo9sH",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "7acb67d6-42e9-4783-b6d3-111ae37a59c2"
      },
      "source": [
        "icecream3.columns"
      ],
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Temperature', 'Revenue'], dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 88
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_d9NuOeM3HWT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "corr = icecream.corr()\n",
        "plt.matshow(corr)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "konheZpsSCyF",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "plt.hist(Rounded, range=(0,600))\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E-ct6a-Jo9LT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "sns.jointplot(x='Temperature',y='Revenue', data=icecream, color = \"pink\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ugVyW9AEqp7F",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "reason_columns = pd.get_dummies(icecream[\"Temperature\"],drop_first = True)"
      ],
      "execution_count": 78,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "m8UU3tjGrHm1",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "reason_columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MI5fBA3jaWrW",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream.isnull().sum()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3ACMBb00sJGS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 387
        },
        "outputId": "f923a935-404c-40ee-b4b5-05e9b0a42a9e"
      },
      "source": [
        "sns.relplot(x='Temperature', y='Revenue', color='green', data=icecream)"
      ],
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x7f39e0daf400>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 65
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 360x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T0FLqzABvT5G",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.model_selection import train_test_split"
      ],
      "execution_count": 115,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tyv0WeBNs6lI",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "icecream4 = icecream.copy()\n",
        "icecream5 = icecream.copy()"
      ],
      "execution_count": 101,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fDouKVD2seC7",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 407
        },
        "outputId": "7129ba56-12e1-4ff0-cb09-b9d954c39cb8"
      },
      "source": [
        "icecream5"
      ],
      "execution_count": 102,
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
              "      <td>534.799028</td>\n",
              "      <td>76.220392</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>625.190122</td>\n",
              "      <td>78.809344</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>660.632289</td>\n",
              "      <td>82.022997</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>487.706960</td>\n",
              "      <td>69.071603</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>316.240194</td>\n",
              "      <td>52.706296</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>524.746364</td>\n",
              "      <td>72.094819</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>755.818399</td>\n",
              "      <td>91.207566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>306.090719</td>\n",
              "      <td>54.658683</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>566.217304</td>\n",
              "      <td>72.252324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>655.660388</td>\n",
              "      <td>84.123925</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Temperature    Revenue\n",
              "0     534.799028  76.220392\n",
              "1     625.190122  78.809344\n",
              "2     660.632289  82.022997\n",
              "3     487.706960  69.071603\n",
              "4     316.240194  52.706296\n",
              "..           ...        ...\n",
              "495   524.746364  72.094819\n",
              "496   755.818399  91.207566\n",
              "497   306.090719  54.658683\n",
              "498   566.217304  72.252324\n",
              "499   655.660388  84.123925\n",
              "\n",
              "[500 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 102
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qZR7xDN90z3V",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train = icecream3.drop(['Revenue'],axis = 1)"
      ],
      "execution_count": 96,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oB3K0gz_t8Dj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "train"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Oarq88mQt9PL",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mJKRn4amtXdq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "test = icecream5.drop(['Temperature'],axis = 1)"
      ],
      "execution_count": 110,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L-dPKTJBtajN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 407
        },
        "outputId": "7142e321-2cab-42ef-9da5-292b858f11e8"
      },
      "source": [
        "icecream5"
      ],
      "execution_count": 108,
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
              "      <td>534.799028</td>\n",
              "      <td>76.220392</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>625.190122</td>\n",
              "      <td>78.809344</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>660.632289</td>\n",
              "      <td>82.022997</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>487.706960</td>\n",
              "      <td>69.071603</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>316.240194</td>\n",
              "      <td>52.706296</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>524.746364</td>\n",
              "      <td>72.094819</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>755.818399</td>\n",
              "      <td>91.207566</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>306.090719</td>\n",
              "      <td>54.658683</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>566.217304</td>\n",
              "      <td>72.252324</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>655.660388</td>\n",
              "      <td>84.123925</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Temperature    Revenue\n",
              "0     534.799028  76.220392\n",
              "1     625.190122  78.809344\n",
              "2     660.632289  82.022997\n",
              "3     487.706960  69.071603\n",
              "4     316.240194  52.706296\n",
              "..           ...        ...\n",
              "495   524.746364  72.094819\n",
              "496   755.818399  91.207566\n",
              "497   306.090719  54.658683\n",
              "498   566.217304  72.252324\n",
              "499   655.660388  84.123925\n",
              "\n",
              "[500 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 108
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tQa12UXOq8U4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 407
        },
        "outputId": "c0b0901b-23ea-4e94-dd11-e8053c6be6f1"
      },
      "source": [
        "train"
      ],
      "execution_count": 93,
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
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>534.799028</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>625.190122</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>660.632289</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>487.706960</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>316.240194</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>495</th>\n",
              "      <td>524.746364</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>496</th>\n",
              "      <td>755.818399</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>497</th>\n",
              "      <td>306.090719</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>498</th>\n",
              "      <td>566.217304</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>499</th>\n",
              "      <td>655.660388</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>500 rows × 1 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     Temperature\n",
              "0     534.799028\n",
              "1     625.190122\n",
              "2     660.632289\n",
              "3     487.706960\n",
              "4     316.240194\n",
              "..           ...\n",
              "495   524.746364\n",
              "496   755.818399\n",
              "497   306.090719\n",
              "498   566.217304\n",
              "499   655.660388\n",
              "\n",
              "[500 rows x 1 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CeqFPMb1sAgx",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "outputId": "224e277d-63c5-4733-9688-2464442e5a3d"
      },
      "source": [
        "test"
      ],
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0      76.220392\n",
              "1      78.809344\n",
              "2      82.022997\n",
              "3      69.071603\n",
              "4      52.706296\n",
              "         ...    \n",
              "495    72.094819\n",
              "496    91.207566\n",
              "497    54.658683\n",
              "498    72.252324\n",
              "499    84.123925\n",
              "Name: Revenue, Length: 500, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 97
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "20NwlW0n0OP6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "x_train, x_test, y_train, y_test = train_test_split(train, test, test_size = 0.3, random_state = 2)"
      ],
      "execution_count": 117,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ks_keQ0A2Gvi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "regr = LinearRegression()"
      ],
      "execution_count": 118,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kFJVUg6B2KPb",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8746dc4f-6d34-483a-b860-52849fd67987"
      },
      "source": [
        "regr.fit(x_train,y_train)"
      ],
      "execution_count": 119,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 119
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jI27b4Fb2Yuj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "predict = regr.predict(x_test)"
      ],
      "execution_count": 120,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R27U_rYx2i7D",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "16c9dc36-239e-48da-f2e4-18dd0db46c68"
      },
      "source": [
        "predict"
      ],
      "execution_count": 121,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[ 90.91909701],\n",
              "       [ 79.09687039],\n",
              "       [ 85.39691645],\n",
              "       [ 77.11702817],\n",
              "       [ 72.5158534 ],\n",
              "       [ 64.00474581],\n",
              "       [ 80.52916491],\n",
              "       [ 60.3751967 ],\n",
              "       [ 95.58199555],\n",
              "       [ 80.26328313],\n",
              "       [ 72.70080126],\n",
              "       [ 73.31243669],\n",
              "       [ 52.0770077 ],\n",
              "       [ 63.37265648],\n",
              "       [ 86.46914242],\n",
              "       [ 79.18743869],\n",
              "       [ 69.31288533],\n",
              "       [ 69.75140013],\n",
              "       [ 85.86688594],\n",
              "       [ 71.88469267],\n",
              "       [ 72.38632021],\n",
              "       [ 58.7304795 ],\n",
              "       [ 51.5949614 ],\n",
              "       [ 51.92953417],\n",
              "       [ 45.07831204],\n",
              "       [ 59.15383569],\n",
              "       [ 82.54096086],\n",
              "       [ 64.99031756],\n",
              "       [ 53.42981926],\n",
              "       [ 79.45304733],\n",
              "       [ 67.63383627],\n",
              "       [ 65.01513838],\n",
              "       [ 75.42696164],\n",
              "       [ 73.71213348],\n",
              "       [ 79.94983641],\n",
              "       [ 62.09892799],\n",
              "       [ 68.3657628 ],\n",
              "       [ 76.40064394],\n",
              "       [ 51.44456617],\n",
              "       [ 73.73120516],\n",
              "       [ 72.84091156],\n",
              "       [ 72.10379617],\n",
              "       [ 65.92928047],\n",
              "       [ 82.96908146],\n",
              "       [ 80.39780859],\n",
              "       [ 80.91744624],\n",
              "       [ 66.87110768],\n",
              "       [ 51.89468897],\n",
              "       [ 68.81906678],\n",
              "       [ 70.84705467],\n",
              "       [ 86.92119009],\n",
              "       [ 81.03503216],\n",
              "       [ 62.37345111],\n",
              "       [ 65.99423691],\n",
              "       [ 76.90296195],\n",
              "       [ 96.45652399],\n",
              "       [ 48.54767955],\n",
              "       [ 52.42819592],\n",
              "       [ 91.31234431],\n",
              "       [ 81.71356293],\n",
              "       [ 53.43963275],\n",
              "       [ 90.66391456],\n",
              "       [ 70.00935459],\n",
              "       [ 71.234028  ],\n",
              "       [ 75.66104228],\n",
              "       [ 71.98395684],\n",
              "       [ 67.92888466],\n",
              "       [ 69.8656356 ],\n",
              "       [ 73.47108627],\n",
              "       [ 66.41328643],\n",
              "       [ 48.91686139],\n",
              "       [ 77.72113186],\n",
              "       [ 53.30047938],\n",
              "       [ 72.81519477],\n",
              "       [ 62.83659144],\n",
              "       [ 55.28686284],\n",
              "       [ 64.44488538],\n",
              "       [103.66649991],\n",
              "       [ 82.26902693],\n",
              "       [ 61.18712332],\n",
              "       [108.93425738],\n",
              "       [ 78.20080938],\n",
              "       [ 68.17561138],\n",
              "       [ 67.50766928],\n",
              "       [ 73.5627248 ],\n",
              "       [ 93.4746344 ],\n",
              "       [ 57.86453594],\n",
              "       [ 68.32229844],\n",
              "       [ 62.40738345],\n",
              "       [ 73.03164161],\n",
              "       [ 83.45486566],\n",
              "       [ 68.01597278],\n",
              "       [ 73.30407355],\n",
              "       [ 62.05833274],\n",
              "       [ 78.39017886],\n",
              "       [ 55.58247545],\n",
              "       [ 88.31197589],\n",
              "       [103.11572079],\n",
              "       [ 85.94428392],\n",
              "       [ 79.95509267],\n",
              "       [ 82.98125684],\n",
              "       [ 77.16199358],\n",
              "       [ 80.79852831],\n",
              "       [ 63.3308687 ],\n",
              "       [ 77.3055309 ],\n",
              "       [ 62.17061165],\n",
              "       [ 76.36215587],\n",
              "       [ 82.70136344],\n",
              "       [ 86.4335778 ],\n",
              "       [ 65.97917791],\n",
              "       [ 50.14209443],\n",
              "       [ 99.70821579],\n",
              "       [ 69.47099624],\n",
              "       [102.50554008],\n",
              "       [ 63.13063965],\n",
              "       [ 78.19295607],\n",
              "       [ 31.60728258],\n",
              "       [ 77.96357391],\n",
              "       [ 60.75732433],\n",
              "       [ 77.50272163],\n",
              "       [ 75.37832654],\n",
              "       [ 56.64171489],\n",
              "       [ 71.64230679],\n",
              "       [ 78.02090551],\n",
              "       [ 49.56862535],\n",
              "       [ 74.57984961],\n",
              "       [ 83.28658565],\n",
              "       [ 65.36652627],\n",
              "       [ 68.83200134],\n",
              "       [ 61.54989383],\n",
              "       [ 70.70854618],\n",
              "       [ 95.73151021],\n",
              "       [ 78.83168132],\n",
              "       [ 87.25972102],\n",
              "       [ 86.95176588],\n",
              "       [ 52.70765228],\n",
              "       [ 51.76898745],\n",
              "       [ 51.46242312],\n",
              "       [ 79.16214967],\n",
              "       [101.15221393],\n",
              "       [ 42.03343194],\n",
              "       [ 72.53766079],\n",
              "       [ 71.91632087],\n",
              "       [ 55.828836  ],\n",
              "       [ 74.38022668],\n",
              "       [104.98980909],\n",
              "       [ 64.64926675],\n",
              "       [ 70.05061471],\n",
              "       [ 60.25309831],\n",
              "       [ 56.63797785]])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2p3uK93K28eU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "0ce23e17-e8e4-4876-8d0b-9523a4e53fd3"
      },
      "source": [
        "regr.score(x_test,y_test )"
      ],
      "execution_count": 122,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.9753630304516299"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 122
        }
      ]
    }
  ]
}
