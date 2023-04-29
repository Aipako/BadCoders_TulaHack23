using TBotService.Controllers;

using System.Linq.Expressions;
using System.Linq;
namespace TBotService.Models
{
    public class GoodUpdater
    {
        private static GoodUpdater _selfInstance;
       
        private GoodUpdater() 
        {
        }

        public static GoodUpdater GetInstance()
        {
            if (_selfInstance == null)
                _selfInstance = new GoodUpdater();
            return _selfInstance;
        }

        public bool UpdateGood(int userId, string url, int newPrice, out bool isSale)
        {
            isSale = false;

            var good = DbController.GetInstance().GetGoodByUrlnId(userId, url);

            if(good == null)
                return false;

            if(good.MedianPrice != null &&ApplySaleProperty(newPrice, (int)good.MedianPrice))
            {
                isSale = true;
            }

            good.Price = newPrice;

            if(good.History != null)
            {
                good.History.Add(newPrice);
            }
            else
            {
                good.History = new List<int> { newPrice };
            }

            good.MedianPrice = GetMedian(good.History);

            DbController.GetInstance().UpdateGood(good);

            return true;

        }

        private bool ApplySaleProperty(int newPrice, int oldPrice)
        {
            // TODO: Realise normal sale detect mechanism

            if (newPrice < oldPrice)
                return true;
            else
                return false;
        }

        private int GetMedian(IEnumerable<int> source)
        {
            int decimals = source.Count();
            if (decimals != 0)
            {
                var midpoint = (decimals - 1) / 2;
                var sorted = source.OrderBy(n => n);
                var median = sorted.ElementAt(midpoint);
                if (decimals % 2 == 0)
                {
                    median = (median + sorted.ElementAt(midpoint + 1)) / 2;
                }

                return median;
            }
            else
            {
                throw new InvalidOperationException("Sequence contains no elements");
            }

        }
    }
}
