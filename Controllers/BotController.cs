using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Net;
using System.Text.Json;
using TBotService.Models;

namespace TBotService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class BotController : ControllerBase
    {
        [HttpPost("addgood", Name = "AddGood")]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(List<GoodClass>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult AddGood(string packedGood)
        {
            try
            {
                DbController.GetInstance().AddGoodToDB((GoodClass)JsonSerializer.Deserialize(packedGood, typeof(GoodClass)));
                return Ok();
            }
            catch (Exception ex)
            {
                return Problem(ex.Message);
            }
        }

        [HttpPost("deletegood", Name = "DeleteGood", Order = 1)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult DeleteGood(int packedGood)
        {
            try
            {
                DbController.GetInstance().DeleteGoodFromDB((GoodClass)JsonSerializer.Deserialize(packedGood, typeof(GoodClass)));
                return Ok();
            }
            catch (Exception ex)
            {
                return Problem(ex.Message);
            }
        }

        [HttpGet("getgoods",Name = "GetUserGoods", Order = 2)]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(List<GoodClass>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult GetGoods(int userId)
        {
            try
            {
                return Ok(DbController.GetInstance().GetGoodsByUser(userId));
            }
            catch (Exception ex)
            {
                return Problem(ex.Message);
            }
        }
    }
}
