    using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.VisualBasic;
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
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult AddGood(string packedGood)
        {
            try
            {
                DbController.GetInstance().AddGoodToDB(JsonSerializer.Deserialize<GoodClass>(packedGood));
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
        public IActionResult DeleteGood(string packedGood)
        {
            try
            {
                DbController.GetInstance().DeleteGoodFromDB(JsonSerializer.Deserialize<GoodClass>(packedGood));
                return Ok();
            }
            catch (Exception ex)
            {
                return Problem(ex.Message);
            }
        }

        [HttpGet("getgoods",Name = "GetUserGoods", Order = 2)]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(List<GoodClass>))]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult GetGoods(int userId)
        {
            try
            {
                var result = DbController.GetInstance().GetGoodsByUser(userId);

                if(result.Count() == 0)
                    return NotFound();

                return Ok(result);
            }
            catch (Exception ex)
            {
                return Problem(ex.Message);
            }
        }
    }
}
