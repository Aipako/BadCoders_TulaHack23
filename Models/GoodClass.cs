using System.Data.SqlClient;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace TBotService.Models
{
    [Serializable()]
    public class GoodClass
    {
        [JsonPropertyName("UserId")]
        [JsonInclude]
        public int UserId { get; set; }

        [JsonPropertyName("Url")]
        [JsonInclude]
        public string Url { get; set; }

        [JsonPropertyName("Price")]
        [JsonInclude]
        public int? Price { get; set; }

        [JsonPropertyName("MedianPrice")]
        [JsonInclude]
        public int? MedianPrice { get; set; }

        [JsonPropertyName("History")]
        [JsonInclude]
        public List<int>? History { get; set; }

        public GoodClass(SqlDataReader rdr)
        {
            UserId = Convert.ToInt32(rdr["UserId"]);
            Url = Convert.ToString(rdr["Url"]);
            Price = Convert.ToInt32(rdr["Price"]);
            MedianPrice = Convert.ToInt32(rdr["MedianPrice"]);
            History = JsonSerializer.Deserialize<List<int>>(Convert.ToString(rdr["History"]));

        }

        [JsonConstructor]
        public GoodClass(int userId, string url, int? price = null, int? medianprice = null, List<int>? history = null)
        {
            UserId = userId;
            Url = url;
            Price = price;
            MedianPrice = medianprice;
            History = history;
        }

        [JsonIgnore]
        public bool IncludeFields
        {
            get
            {
                return true;
            }
        }

        public string GetHistoryPacked()
        {
            return JsonSerializer.Serialize(History);
        }

        /*[Serializable]
        public class PriceHistoryClass
        {
            [JsonPropertyName("prices")]
            public int[]? Prices { get; set; }
        }*/

    }
}
