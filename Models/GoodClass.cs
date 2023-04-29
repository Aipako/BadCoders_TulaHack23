using System.Data.SqlClient;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace TBotService.Models
{
    [Serializable()]
    public class GoodClass
    {
        [JsonPropertyName("UserId")]
        public int UserId { get; set; }

        [JsonPropertyName("Url")]
        public string Url { get; set; }

        [JsonPropertyName("Price")]
        public int? Price { get; set; }

        [JsonPropertyName("MedianPrice")]
        public int? MedianPrice { get; set; }

        [JsonPropertyName("PriceHistory")]
        public PriceHistoryClass? PriceHistory { get; set; }

        public GoodClass(SqlDataReader rdr)
        {
            UserId = Convert.ToInt32(rdr["UserId"]);
            Url = Convert.ToString(rdr["Url"]);
            Price = Convert.ToInt32(rdr["Price"]);
            MedianPrice = Convert.ToInt32(rdr["MedianPrice"]);
            PriceHistory = (PriceHistoryClass)JsonSerializer.Deserialize(Convert.ToString(rdr["History"]), typeof(PriceHistoryClass));

        }

        public string GetHistoryPacked()
        {
            return JsonSerializer.Serialize(PriceHistory);
        }

        [Serializable]
        public class PriceHistoryClass
        {
            [JsonPropertyName("prices")]
            public int[]? Prices { get; set; }
        }

    }
}
