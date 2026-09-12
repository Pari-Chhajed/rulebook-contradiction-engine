import json
import time
from engine import engine

def run_evals():
    with open("eval/test_cases.json", "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    correct = 0
    total = len(test_cases)
    
    category_scores = {
        "CONTRADICTION": {"total": 0, "correct": 0},
        "ANSWER": {"total": 0, "correct": 0},
        "REFUSAL": {"total": 0, "correct": 0}
    }

    print("=" * 70)
    print("  RUNNING SYSTEM EVALUATION: THE RULEBOOK THAT ARGUES WITH ITSELF")
    print("=" * 70)

    start_time = time.time()

    for item in test_cases:
        res = engine.query(item["q"])
        expected = item["expected_state"]
        actual = res.state
        
        category_scores[expected]["total"] += 1
        is_match = (expected == actual)
        
        if is_match:
            correct += 1
            category_scores[expected]["correct"] += 1
            status = "[PASS]"
        else:
            status = "[FAIL]"

        print(f"{status} ID: {item['id']} | Expected: {expected:<13} | Actual: {actual:<13} | Q: {item['q'][:40]}...")

    elapsed = round(time.time() - start_time, 2)
    overall_acc = round((correct / total) * 100, 2)

    print("\n" + "=" * 70)
    print("  EVALUATION SUMMARY REPORT")
    print("=" * 70)
    for cat, scores in category_scores.items():
        acc = (scores["correct"] / scores["total"] * 100) if scores["total"] > 0 else 0
        print(f" Category: {cat:<15} | Score: {scores['correct']}/{scores['total']} ({acc:.1f}%)")

    print("-" * 70)
    print(f" Overall Accuracy: {correct}/{total} ({overall_acc}%) in {elapsed}s")
    print("=" * 70)

if __name__ == "__main__":
    run_evals()