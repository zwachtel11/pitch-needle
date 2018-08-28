using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using criticApi.Models;

namespace TodoApi.Controllers
{
    [Route("api/record")]
    [ApiController]
    public class RecordController : ControllerBase
    {
        private readonly CriticContext _context;

        public RecordController(CriticContext context)
        {
            _context = context;

            if (_context.Records.Count() == 0)
            {
                // Create a new TodoItem if collection is empty,
                // which means you can't delete all TodoItems.
                _context.Records.Add(new Record { Album = "Item1" });
                _context.SaveChanges();
            }
        }

        [HttpGet]
        public ActionResult<List<Record>> GetAll()
        {
            List<Record> test = _context.Records.ToList();
            test.Sort((x, y) => y.ReleaseDate.CompareTo(x.ReleaseDate));
            return test;
        }

        [HttpGet("{id}", Name="GetRecord")]
        public ActionResult<Record> GetByID(long id)
        {
            var item = _context.Records.Find(id);
            if (item == null)
            {
                return NotFound();
            }
            return item;
        }
    }
}