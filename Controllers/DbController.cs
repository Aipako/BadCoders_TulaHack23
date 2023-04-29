using Microsoft.AspNetCore.Routing;
using System.Data.SqlClient;
using System.Data;
using TBotService.Models;

namespace TBotService.Controllers
{
    public class DbController
    {
        private static DbController selfInstance;

        private const string _connectionString = "Server=MAXIMPC\\SQLEXPRESS; Database=bot; uid=tbot; pwd=tbotpass;";

        private DbController()
        {
        }

        public static DbController GetInstance()
        {
            if (selfInstance == null)
                selfInstance = new DbController();
            return selfInstance;
        }

        public void InitController()
        {
            if (string.IsNullOrWhiteSpace(_connectionString))
                throw new ArgumentException("Parameter Route cannot be empty");
        }

        public void AddGoodToDB(GoodClass good)
        {
            using (var conn = new SqlConnection(_connectionString))
            {
                conn.Open();
                var cmd = conn.CreateCommand();
                cmd.CommandType = CommandType.Text;
                cmd.CommandText = "insert Goods values (@UserId, @Url," +
                                  "@Price, @MedianPrice, @History)";
                cmd.Parameters.AddWithValue("@UserId", good.UserId);
                cmd.Parameters.AddWithValue("@Url", good.Url);
                cmd.Parameters.AddWithValue("@Price", good.Price);
                cmd.Parameters.AddWithValue("@MedianPrice", good.MedianPrice);
                cmd.Parameters.AddWithValue("@History", good.GetHistoryPacked());
            }
            return;
        }

        public void DeleteGoodFromDB(GoodClass good)
        {
            using (var conn = new SqlConnection(_connectionString))
            {
                conn.Open();
                var cmd = conn.CreateCommand();
                cmd.CommandType = CommandType.Text;
                cmd.CommandText = "delete Goods where UserId=@UserId and " +
                                  "Url=@Url";
                cmd.Parameters.AddWithValue("@UserId", good.UserId);
                cmd.Parameters.AddWithValue("@Url", good.Url);
            }
            return;
        }

        public IEnumerable<GoodClass> GetGoodsByUser(int userId)
        {
            using (var conn = new SqlConnection(_connectionString))
            {
                conn.Open();
                var cmd = conn.CreateCommand();
                cmd.CommandType = CommandType.Text;
                cmd.CommandText = "select * from Goods " +
                                  "where UserId=@UserId";
                cmd.Parameters.AddWithValue("@UserId", userId);

                var result = new List<GoodClass>();
                using (var rdr = cmd.ExecuteReader())
                {
                    while (rdr.Read())
                    {
                        result.Add(new GoodClass(rdr));
                    }
                }

                return result;
            }
            
        }


    }
}
